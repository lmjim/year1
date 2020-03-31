'''CIS 211 Notes

[a-zXY] is all lowercase letters and "X" and "Y"

(boom)* is all repetitions of "boom" so "" and "boom" and "boomboom" etc.

Check out pythex.org or regexr.com or https://www.browserling.com/tools/text-from-regex

Regular expression: xyz(w*)xyz
matches: xyzwwwxyz or xyzxyz or xyzwxyz etc.

Regular expression: (H|h)ello
matches: Hello and hello


Regular expression: (Gg)reat
Ex. Match: GgGgreat

Regular expression: [Gg]reat
Matches: Great and great

Regular expression: (G|g)reat
Matches: Great and great


match = re.match(r"""  # raw text
                [Gg}  # Could be great or REALLY GREAT
                (?P<rs> r+)  # capture them rs     I'm going to tell you want your matches are
                eat
                !
                """, "Grrrreat!", re.VERBOSE)


Regular Expression: (?P<number>[0-9]+) \s* (?P<streetname>[a-zA-Z]+) \s* Street
Willy Wonka
2133 Wonka Street
Philly, PA 83234
Match 1: number     2133
         streetname Wonka

(?P<number>[0-9]+) \s* (?P<streetname>[a-zA-Z]+) \s* Street \n* (?P<city>[a-zA-Z]+)
Willy Wonka
2133 Wonka Street
Philly, PA 83234
Match 1: city       Philly
         number     2133
         streetname Wonka


Regular Expression: (?P<username>[^\s@]+)@(?P<mailhost>[a-zA-Z_.]+)
wally_87@gmail.com
Match 1: username wally_87
         mailhost gmail.com

(?P<username>[^\s@]+)@(?P<mailhost>[a-zA-Z_.]+.[a-zA-Z_.]+)
wally_87@gmail.com
wallywankette@cs.uoregon.edu
Match 1
username	wally_87
mailhost	gmail.com
Match 2
username	wallywankette
mailhost	cs.uoregon.edu



\s*  # all whitespace so lots of spaces, tabs, single space, single tab, new line, many blank lines, or no whitespace
\s+  # at least one whitespace character
\n*  # many new (blank) lines or single new line
\s   # single space
\n   # one new line
\w*  # word (anything that's not whitespace)




ASSM_PAT = re.compile(r"""
    (
    (?P<label>[a-zA-Z]\w*):
    )? /s*
    ( (?P<opcode> [a-zA-Z]+)
    (\/ (?P<predicate> [a-zA-Z]+) )?
    \s*
    (?P<target> r[0-9]+),
    (?P<src1> r[0-9]+),
    (?P<src2> r[0-9]+)
    (\[(?P<offset>[-]?[0-9]+) \])?
    )?
    ( \s* (?P<comment>[\#:].*) )?
    \s*$
    """,re.X)

frobnaz: ADD/NZ r1,r0,r2[-34]  # A comment

'''
