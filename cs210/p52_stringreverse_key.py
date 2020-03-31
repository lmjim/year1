'''
Reverse a string (+ challenges)
CIS 210 F17 Project 5-2

Author: [Solution]

Recursive and iterative functions
to reverse a string, including
comprehensive test cases.

Practice:
-designing algorithms
-recursive algorithms, functions
-testing
'''
import doctest

def strReverseI(s):
    '''(str) -> str

    Iterative function to reverse s;
    return the reversed string.

    Testing:
    Basic - 'abc', 'hello'
    Boundary - ''
    Equivalence classes - alpha, non-alpha

    >>> strReverseI('abc')
    'cba'
    >>> strReverseI('hello')
    'olleh'
    >>> strReverseI('')
    ''
    >>> strReverseI('CIS 210')
    '012 SIC'
    '''
    rstr = ''
    for ch in s:
        rstr = ch + rstr

    return rstr

def strReverseR(s):
    '''(str) -> str

    Recursive function to reverse s;
    return the reversed string.

    Testing:
    Basic - 'abc', 'hello'
    Boundary - ''
    Equivalence classes - alpha, non-alpha

    >>> strReverseI('abc')
    'cba'
    >>> strReverseI('hello')
    'olleh'
    >>> strReverseI('')
    ''
    >>> strReverseI('CIS 210')
    '012 SIC'
    '''
    if (len(s) == 1) or (len(s) == 0):
        return s
    else:
        return strReverseR(s[1:]) + s[0]

def main():
    print(doctest.testmod()); print()
    s = input('Enter string: ')
    print(strReverseR(strReverseI(s)))

    return None

if __name__ == '__main__':
    main()

# challenge

def hailstoneR(n):
    '''(int) -> None

    hailstone algorithm always converges
    on 1, though no proof of this

    >>> hailstoneR(5)
    5
    16
    8
    4
    2
    1
    '''
    # can define a short auxiliary function
    # in an enclosing function.
    # even finds n in the "enclosing" scope.
    # (Python searches local-enclosing-global-builtin)
    def even():
        return (n % 2) == 0
    
    if n == 1:
        print(n)
    else:
        print(n)
        if even():
            hailstoneR(n//2)
        else:
            hailstoneR(3*n+1)

    return None

def hailstoneI(n):
    '''(int) -> None

    hailstone algorithm always converges
    on 1, though no proof of this

    >>> hailstoneI(5)
    5
    16
    8
    4
    2
    1
    '''
    def even():
        return (n % 2) == 0
    
    while n > 1:
        print(n)
        if even():
            n = n // 2
        else:
            n = 3*n + 1
            
    print(n)
    return None

#print(doctest.testmod())



    
