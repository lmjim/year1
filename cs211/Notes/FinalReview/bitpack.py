"""encoding and decoding 9 bits
aaa bbb cc"""

from typing import Tuple


def pack(a:int, b: int, c: int) -> int:
    """Example: Suppose we are packing 3, 3, 2
    3 is 011
    2 is 10"""
    a = a << 5  # Now a is 011 000 00
    b = b << 2  # Now b is     011 00
                # c is             10
    return a | b | c     # 011 011 10 is returned


def unpack(word: int) -> Tuple[int, int, int]:
    a = word >> 5      # Now a is 011  (011 10 gets pushed off)
    b = word >> 2 & 7  # Now b is 011  (10 gets pushed off and 011 011 gets & with 000 111)
    c = word & 3       # Now c is  10  (011 011 10 gets & with 000 000 11)
    return a, b, c


def testit(x,y,z):
    print("Testing pack/unpack of {},{},{}".format(x,y,z))
    assert 0 <= x <= 7, "Test case valid"
    assert 0 <= y <= 7, "Test case valid"
    assert 0 <= z <= 3, "Test case valid"
    packed = pack(x,y,z)
    a,b,c = unpack(packed)
    assert a==x and b==y and c==z, "Unpack is inverse of pack"


testit(7,7,3)
testit(1,1,1)
testit(0,0,0)
testit(5,7,2)
testit(0,7,3)
testit(7,0,3)
testit(7,7,0)
