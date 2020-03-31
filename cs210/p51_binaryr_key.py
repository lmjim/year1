'''
Number conversion - recursive.
Testing.

CIS 210 F17 Project 5-1.

Author: [Solution]

Credits:  N/A

"Encode" and "decode" decimal numbers to
binary representation.

Add recursive encoding function.
Examples of use in function docstrings include various
test cases - basic, edge, examples from equivalence
classes for input and expected results.

Credits: N/A
'''
import doctest

def dtob(n):
    '''(int) -> str

    Convert non-negative integer n to binary string.

    Testing:
    Simple - 4
    Boundary - 0, 1, 2
    Equivalence classes - odd, even integers

    >>> dtob(4)
    '100'
    >>> dtob(0)
    '0'
    >>> dtob(1)
    '1'
    >>> dtob(2)
    '10'
    >>> dtob(27)
    '11011'
    >>> dtob(44)
    '101100'
 
    '''
    assert n >= 0
    assert isinstance(n, int)

    if n == 0:
        b = '0'
    else:
        b = ''
        next_n = n
        while next_n > 0:
            r = next_n % 2
            b = str(r) + b
            next_n = next_n // 2

    return b


def dtobr(n):
    '''(int) -> str

    Use recursive algorithm to
    convert n > 0 to binary string.

    Testing:
    Simple - 4
    Boundary - 0, 1, 2
    Equivalence classes - odd, even integers

    >>> dtob(4)
    '100'
    >>> dtob(0)
    '0'
    >>> dtob(1)
    '1'
    >>> dtob(2)
    '10'
    >>> dtob(27)
    '11011'
    >>> dtob(44)
    '101100'
    '''
    if n < 2:
        return str(n)
    else:
        return dtobr(n // 2) + str(n % 2)

def btod(b):
    '''(str) -> integer

    Convert binary string to decimal integer.

    Testing:
    Simple - '100'
    Boundary - '0000', '11111'
    Equivalence classes - even, odd

    >>> btod('100')
    4
    >>> btod('11111')
    31
    >>> btod('0000')
    0
    >>> btod('11011')
    27
    >>> btod('101100')
    44
    '''
    for bit in b:
        assert bit in '01'
    
    dn = 0
    bctr = len(b) - 1
    for bit in b:
        dn += int(bit) * (2**bctr)
        bctr -= 1

    return dn

def main():
    '''() -> None

    check binary conversion functions
    by encoding and decoding number
    '''
    print(doctest.testmod())
    d = int((input('Enter non-negative integer: ')))
    b = dtobr(d)
    print('Binary format is {}'.format(b))
    checkd = btod(b)
    print('Back to decimal: {}'.format(checkd))
    return None


if __name__ == '__main__':
    main()
  
