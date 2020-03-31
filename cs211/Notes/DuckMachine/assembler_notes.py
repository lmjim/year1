import re

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


def resolve_labels(lines) -> tuple:
    """Error check and keep track of the number of errors
    Something with incorrect spelling is an error
    Something that doesn't have enough arguments is an error
    Something that has too many arguments is an error
    Keep track of each line
    But don't count comment lines
    Returns (table of lines, # of errors)"""
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
    """Go through each line
    Does this line have a symbolic pattern?
    If so, call build_resolved"""
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
    """Use if you have found JUMP, STORE, or LOAD
    Changes JUMP, STORE, and LOAD
    Goes through each line and finds labels
    No change if it is DATA, FULL, or COMMENT
    If it is SYM then make changes
    STORE and LOAD have same change
    JUMP has another change
    For STORE and LOAD:
    use .format on a line to say 'have this label be the label I still had
    but change the operator and the operand and the memory associated with the pc'
    .format(label,op,target,pc_mem)
    For JUMP:
    .format(label,predicate,pc_mem)
    # /N is the predicate and is used if you are going backwards (don't need if going forward)
    """
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
        pc_mem = symtab[symbol]
        pc_mem -= address
    if op == ("LOAD" or "STORE"):
        return "{} {} {},r0,r15[{}]".format(label, op, target, pc_mem)
    if op == "JUMP":
        return "{} ADD{} r15,r0,r15[{}]".format(label, predicate, pc_mem)


def main():
    """"Assemble a Duck Machine program"""
    args = cli()
    lines = args.sourcefile.readlines()
    symtab = resolve_labels(lines)[0]
    transform_instructions(lines, symtab)
    for line in lines:
        print(line.strip(), file=args.objfile)


def test_match(s: str):
    match = ASM_SYM_PAT.match(s)
    if match:
        print("Matched {}, \nfields {}".format(s,match.groupdict()))
    else:
        print("Didn't match {}".format(s))


test_match("Lab: JUMP/Z foo")
test_match("    JUMP/Z foo")
test_match("    LOAD r0,foo")
test_match("STORE r1,bar")
test_match("LOAD  r2,initial      # We will double this value repeatedly")
test_match("  JUMP/N Loop           # repeat")
