"""
Assembler Pass 1

Takes .asm files and writes .dasm files

Author: Lily Jim
"""
import argparse

from typing import List
from enum import Enum, auto

import sys
import re
import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


# Configuration constants
ERROR_LIMIT = 5    # Abandon assembly if we exceed this


class SyntaxError(Exception):
    pass


# To simplify client code, we'd like to return a dict with
# the right fields even if the line is syntactically incorrect.
DICT_NO_MATCH = {'label': None, 'opcode': None, 'predicate': None,
                 'target': None, 'src1': None, 'src2': None,
                 'offset': None, 'comment': None }


class AsmSrcKind(Enum):
    """Distinguish which kind of assembly language instruction
    we have matched.  Each element of the enum corresponds to
    one of the regular expressions below.
    """
    # Blank or just a comment, optionally with a label
    COMMENT = auto()
    # Fully specified  (all addresses resolved)
    FULL = auto()
    # A data location, not an instruction
    DATA = auto()
    # Includes symbols (STORE, JUMP, LOAD)
    SYM = auto()


# Lines that contain only a comment (and possibly a label).
# This includes blank lines and labels on a line by themselves.
ASM_COMMENT_PAT = re.compile(r"""
   # Optional label 
   (
     (?P<label> [a-zA-Z]\w*):
   )?
   \s*
   # Optional comment follows # or ; 
   (
     (?P<comment>[\#;].*)
   )?       
   \s*$             
   """, re.VERBOSE)


# Instructions with fully specified fields. We can generate
# code directly from these.  In the transformation phase we
# pass these through unchanged, just keeping track of how much
# room they require in the final object code.
ASM_FULL_PAT = re.compile(r"""
   # Optional label 
   (
     (?P<label> [a-zA-Z]\w*):
   )?
   # The instruction proper 
   \s*
    (?P<opcode>    [a-zA-Z]+)           # Opcode
    (/ (?P<predicate> [a-zA-Z]+) )?   # Predicate (optional)
    \s+
    (?P<target>    r[0-9]+),            # Target register
    (?P<src1>      r[0-9]+),            # Source register 1
    (?P<src2>      r[0-9]+)             # Source register 2
    (\[ (?P<offset>[-]?[0-9]+) \])?     # Offset (optional)
   # Optional comment follows # or ; 
   (
     \s*
     (?P<comment>[\#;].*)
   )?       
   \s*$             
   """, re.VERBOSE)


# Defaults for values that ASM_FULL_PAT makes optional
INSTR_DEFAULTS = [('predicate', 'ALWAYS'), ('offset', '0')]


# A data word in memory; not a DM2018W instruction
ASM_DATA_PAT = re.compile(r""" 
   # Optional label 
   (
     (?P<label> [a-zA-Z]\w*):
   )?
   # The instruction proper  
   \s*
    (?P<opcode>    DATA)           # Opcode
   # Optional data value
   \s*
   (?P<value>  (0x[a-fA-F0-9]+)
             | ([0-9]+))?
    # Optional comment follows # or ; 
   (
     \s*
     (?P<comment>[\#;].*)
   )?       
   \s*$             
   """, re.VERBOSE)


ASM_SYM_PAT = re.compile(r"""
   # Optional label 
   (
     (?P<label> [a-zA-Z]\w*):
   )?
   # The instruction proper 
   \s*
    (?P<opcode>    (JUMP)|(STORE)|(LOAD))   # Opcode
    (/ (?P<predicate> [a-zA-Z]+) )?         # Predicate (optional)
    \s+
    ((?P<target>    r[0-9]+),)?             # Target register (optional)
    (?P<symbol>     [a-zA-Z]\w*)            # Symbol
   # Optional comment follows # or ; 
   (
     \s*
     (?P<comment>[\#;].*)
   )?       
   \s*$             
   """, re.VERBOSE)


PATTERNS = [(ASM_FULL_PAT, AsmSrcKind.FULL),
            (ASM_DATA_PAT, AsmSrcKind.DATA),
            (ASM_COMMENT_PAT, AsmSrcKind.COMMENT),
            (ASM_SYM_PAT, AsmSrcKind.SYM)
            ]


def parse_line(line: str) -> dict:
    """Parse one line of assembly code.
    Returns a dict containing the matched fields,
    some of which may be empty.  Raises SyntaxError
    if the line does not match assembly language
    syntax. Sets the 'kind' field to indicate
    which of the patterns was matched.
    """
    log.debug("\nParsing assembler line: '{}'".format(line))
    # Try each kind of pattern
    for pattern, kind in PATTERNS:
        match = pattern.fullmatch(line)
        if match:
            fields = match.groupdict()
            fields["kind"] = kind
            log.debug("Extracted fields {}".format(fields))
            return fields
    raise SyntaxError("Assembler syntax error in {}".format(line))


def resolve_labels(lines: List[str]) -> tuple:
    """Creates a table of labels which should match
    the symbols in lines. Also looks for errors."""
    error_count = 0
    symtab = {}
    address = 0
    for lnum in range(len(lines)):
        line = lines[lnum]
        log.debug("Processing line {}: {}".format(lnum, line))
        try:
            fields = parse_line(line)
            if fields["label"]:
                if fields["label"] in symtab:
                    error_count += 1
                    print("Duplication Error in line {}: {}".format(lnum, line))
                else:
                    symtab[fields["label"]] = address
            if fields["kind"] != AsmSrcKind.COMMENT:
                address += 1
        except SyntaxError as e:
            error_count += 1
            print("Syntax error in line {}: {}".format(lnum, line))
        except KeyError as e:
            error_count += 1
            print("Unknown word in line {}: {}".format(lnum, e))
        except Exception as e:
            error_count += 1
            print("Exception encountered in line {}: {}".format(lnum, e))
        if error_count > ERROR_LIMIT:
            print("Too many errors; abandoning")
            sys.exit(1)
    return (symtab, error_count)


def transform_instructions(lines, symtab):
    """Change lines with symbols to lines without symbols"""
    address = 0
    for lnum in range(len(lines)):
        line = lines[lnum]
        fields = parse_line(line)
        if fields["kind"] == AsmSrcKind.SYM:
            lines[lnum] = build_resolved(fields, address, symtab)
        if fields["kind"] != AsmSrcKind.COMMENT:
            address += 1
    return None


def build_resolved(fields, address, symtab):
    """Takes a string with a symbol and changes
    the symbol to a readable instruction"""
    label = fields["label"] or ""
    op = fields["opcode"]
    assert op == "LOAD" or "STORE" or "JUMP", "Operation is not LOAD, STORE, or JUMP"
    symbol = fields["symbol"]
    target = fields["target"] or "r0"
    if fields["predicate"]:
        predicate = "/{}".format(fields["predicate"])
    else:
        predicate = ""
    pc_mem = 0
    if symbol in symtab:
        pc_mem = symtab[symbol] - address
    if op == "LOAD" or op == "STORE":
        return "{} {} {},r0,r15[{}]".format(label, op, target, pc_mem)
    if op == "JUMP":
        return "{} ADD{} r15,r0,r15[{}]".format(label, predicate, pc_mem)


def cli() -> object:
    """Get arguments from command line"""
    parser = argparse.ArgumentParser(description="Duck Machine Assembler (pass 2)")
    parser.add_argument("sourcefile", type=argparse.FileType('r'),
                            nargs="?", default=sys.stdin,
                            help="Duck Machine assembly code file")
    parser.add_argument("dasmfile", type=argparse.FileType('w'),
                            nargs="?", default=sys.stdout,
                            help=".dasm file output")
    args = parser.parse_args()
    return args


def main():
    """"Assemble a Duck Machine program"""
    args = cli()
    lines = args.sourcefile.readlines()
    symtab, errors = resolve_labels(lines)
    if errors == 0:
        transform_instructions(lines, symtab)
        for line in lines:
            print(line.strip(), file=args.dasmfile)


if __name__ == "__main__":
    main()
