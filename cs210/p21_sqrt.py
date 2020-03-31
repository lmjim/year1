'''
Square Root
CIS 210 F17 Project 2-1

Author: Lily Jim

Credits: N/A

Approximate the square root of a number and compare it to the actual square root
'''
import math

def mysqrt(n, k):
    '''(int, int) -> float
    Approximates the square root of a number, n,
    iterating the process k times
    returning the final approximation, x
    >>> mysqrt(25, 5)
    5.000023178253949
    >>> mysqrt(25, 10)
    5.0
    >>> mysqrt(10000, 10)
    100.00000025490743
    >>> mysqrt(10000, 11)
    100.0
    '''
    x = 1
    for i in range(k):
        x = 0.5 * (x + (n/x))

    return x

def sqrt_compare(n, k):
    '''(int, int) -> None
    Runs n and k through 'mysqrt' and compares that value
    to the value math lib sqrt gets for n
    Prints the comparison and a percent error
    Returns none
    >>> sqrt_compare(10000, 8)
    For 10000 using 8 iterations:
    mysqrt value is: 101.20218365353946
    math lib sqrt value is: 100.0
    This is a 1.2 percent error.
    >>> sqrt_compare(25, 5)
    For 25 using 5 iterations:
    mysqrt value is: 5.000023178253949
    math lib sqrt value is: 5.0
    This is a 0.0 percent error.
    '''

    z = math.sqrt(n)
    x = mysqrt(n, k)
    a = abs(z - x)
    b = (a / z) * 100
    y = round(b, 2)

    print('For', n, 'using', k, 'iterations:')
    print('mysqrt value is:', x)
    print('math lib sqrt value is:', z)
    print('This is a', y, 'percent error.')
    
    return None

def mysqrtp(n, p):
    '''(int, num) -> float, int
    Approximate the square root of n with a precision of p
    Returns the approximate square root, x, and the number of
    iterations, k, that it took to get x
    >>> mysqrtp(125348, .01)
    (354.0518885182295, 11)
    >>> mysqrtp(16, .001)
    (4.000000636692939, 5)
    >>> mysqrtp(25, .0001)
    (5.000023178253949, 5)
    '''
    k = 0
    x = 1
    z = math.sqrt(n)
    
    while (abs(z - x)) > p:
        x = 0.5 * (x + (n/x))
        k += 1
        
    return x, k



