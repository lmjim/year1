'''
Show Approximation of Pi
CIS 210 F17 Project 3-2

Author: Lily Jim

Credits: Based on code on p.78 Miller and Ranum text

Show in Turtle the processes of approximating pi
using the Monte Carlo algorithm
And compare approximated value of pi to math.pi
'''

from turtle import *
import math
import random

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


def showMontePi(numDarts):
    ''' (int) -> float
    Visually show Monte Carlo's algorithm to approximate pi in Turtle
    Points within the circle will be blue and points outside will be red
    Compares approximate value of pi with math lib pi, printing a percent error
    Returns the approximated value after Turtle finishes running
    Note: due to randomness, approximations may vary slightly
    each time the function executes
    >>> showMontePi(100)
    #Darts are thrown in turtle window
    With 100 iterations:
    my approximate value for pi is: 3.32
    math lib pi value is: 3.141592653589793
    This is a 5.68 percent error.
    >>> showMontePi(500)
    #Darts are thrown in turtle window
    With 500 iterations:
    my approximate value for pi is: 3.216
    math lib pi value is: 3.141592653589793
    This is a 2.37 percent error.
    >>> showMontePi(1000)
    #Darts are thrown in turtle window
    With 1000 iterations:
    my approximate value for pi is: 3.188
    math lib pi value is: 3.141592653589793
    This is a 1.48 percent error.
    '''
    # set up canvas and turtle
    # to animate the algorithm;
    # draw x, y axes
    
    wn = Screen()
    wn.setworldcoordinates(-2, -2, 2, 2)

    speed('fastest'); hideturtle()
    penup()

    goto(-1, 0)
    pendown()
    goto(1, 0)
    penup()
    goto(0, 1)
    pendown()
    goto(0, -1)
    penup()
    goto(0, -1)

    # pen should stay up for drawing darts
 
    inCircleCt = 0

    # throw the darts and check whether
    # they landed on the dart board and
    # keep count of those that do   
    for i in range(numDarts):
        x = random.random()
        y = random.random()

        # show the dart on the board
        if isInCircle(x, y, 1) == 1:
            inCircleCt += 1
            color('blue')
        else:
            color('red')

        goto(x, y)
        dot()

    # calculate approximate pi
    approxPi = inCircleCt/numDarts * 4

    # compare approxPi to math.pi
    difference = abs(math.pi - approxPi)
    percentError = (difference / math.pi) * 100
    roundedError = round(percentError, 2)
    
    print('With', numDarts, 'iterations:')
    print('my approximate value for pi is:', approxPi)
    print('math lib pi value is:', math.pi)
    print('This is a', roundedError, 'percent error.')

    wn.exitonclick()

    return approxPi


showMontePi(1000)
