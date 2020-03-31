'''
Approximate Pi
CIS 210 F17 Project 3-1

Author: Lily Jim

Credits: Based on code on p.74 Miller and Ranum text.

Approximate the value of Pi using the Monte Carlo algorithm
'''

import random
import math

def isInCircle(x, y, r):
    ''' (float, float, float) -> bool
    Determine whether a point is inside a circle or not
    Return true if the point is in the circle
    Return false if the point is not in the circle
    >>> isInCircle(0, 0, 1)
    True
    >>> isInCircle(.5, .5, 1)
    True
    >>> isInCircle(1, 1, 1)
    False
    '''

    distance = math.sqrt(x ** 2 + y ** 2)
    inside = (distance <= r)
    
    return inside

def montePi(numDarts):
    ''' (int) -> float
    Returns an approximation of pi using a Monte Carlo algorithm
    by seeing how many points in a square fall within a circle
    Note: due to randomness, approximations may vary slightly
    each time the function executes
    >>> montePi(1000)
    3.084
    >>> montePi(1000)
    3.18
    >>> montePi(1000000)
    3.142692
    >>> montePi(1000000)
    3.141856
    '''

    inCircleCt = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        inCircleCt += isInCircle(x, y, 1) #When in the circle 1 will be added,
                                          #when not in the circle 0 will be added

    approxpi = inCircleCt/numDarts * 4
    
    return approxpi

print(isInCircle(0, 0, 1))    
print(isInCircle(.5, .5, 1))
print(isInCircle(1, 2, 1))
print(montePi(100))
print(montePi(10000))
print(montePi(10000000))

