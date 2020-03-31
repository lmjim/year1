'''
Binary Encoding and Decoding
CIS 210 F17 Project 4-2

Author: Lily Jim

Credits: N/A

Switch between decimal representation and binary representation
'''
import doctest

def dtob(n):
    '''(int) -> str
    Take a decimal representation of a non-negative integer
    and change it to binary represetation.
    Return the binary string
    >>> dtob(27)
    '11011'
    >>> dtob(0)
    '0'
    >>> dtob(1)
    '1'
    >>> dtob(2)
    '10'
    '''
    string = ''
    while n > 0:
        digit = n % 2
        n = n // 2
        digit = str(digit)
        string = digit + string
    if string == '':
        string = '0'
        
    return string

def btod(b):
    ''' (str) -> int
    Take a string of a number in binary and change it to
    decimal representation. Return the non-negative integer
    >>> btod('0000')
    0
    >>> btod('1101')
    13
    >>> btod('111111')
    63
    '''
    decimal = 0
    for i in range(len(b)):
        value = int(b[i])
        power = 2 ** ((len(b))-i-1)
        decimal += (power * value)

    return decimal
        

def main():
    ''' () -> None
    Ask for a non-negative integerand change it to binary and back
    '''
    print('What is the decimal representation?')
    n = int(input())
    b = dtob(n)
    print('Binary representation:', b)
    print('Decimal representation:', btod(b))
    
    return None

print(doctest.testmod())
main()
