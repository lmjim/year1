'''
Art Show
CIS 210 F17 Project 2-2

Author: Lily Jim

Credits: N/A

Have turtle draw a simple line drawing
'''
from turtle import *

def art_show(boat, flag):
    ''' (str, str) -> None
    Draws a boat on water in the turtle window
    Returns None
    >>> art_show('red', 'green')
    Red boat with green flag drawn in turtle window
    >>> art_show('green', 'yellow')
    Green boat with yellow flag drawn in turtle window
    '''
    pensize(5)

    #Draw Hull:
    right(90)
    pencolor(boat)
    for i in range(26):
        forward(10)
        left(180 / 25)

    goto(0,0)

    #Draw Mast:
    penup()
    goto(75, 0)
    pendown()
    pencolor('black')
    right(7)
    forward(100)

    #Draw Flag:
    right(115)
    pencolor(flag)
    forward(50)
    right(115)
    forward(55)

    #Draw Water:
    penup()
    goto(-50, -100)
    right(175)
    pencolor('blue')
    pendown()
    for i in range(4):
        forward(50)
        right(90)
        forward(50)
        left(90)
    
    return None

