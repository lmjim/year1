"""Imagine we didn't have the built-in functions 'hex' or 'format'
we can still easily translate an integer to hexadecimal"""


DIGITS = "0123456789ABCDEF"


def hexify(i:int) -> str:
    hex = ""
    if i == 0:
        return "0"
    while i > 0:
        i_low = i & 15
        i_low = DIGITS[i_low]
        hex = i_low + hex
        i = i >> 4
    return hex


def hexify2(i):
    if i == 0:
        return ""  # If orignial number is 0 then you will get an empty string NOT 0
    else:
        return hexify(i >> 4) + DIGITS[i & 15]


print(hexify(0xf3e45a))
# Expected output F3E45A


"""
18 base 10
into base 5:
33

13 base 5
into base 10:
8

>>> x = 0xA7
>>> x
167
>>> x_low = x & 15
>>> x_low
7
>>> digits = "0123456789ABCDEF"
>>> digits[x_low]
'7'
>>> x_high = (x >> 4) & 15
>>> x_high
10
>>> digits[x_high]
'A'
"""