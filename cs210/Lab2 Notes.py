'''
(str) -> str #string to string
Expressions have return values
Return value acts as an anchor
Print is a Side Effect
'''
def iPrint(msg):
    print("Error diagnostics", msg); #Msg could be "memory allocatoin failure
    return None
'''
Built in functions like print, round, abs, str, etc.
Libraries of other useful functions available to import
    import math #don't include the .py extension
    math. #remember the DOT! ex. math.sqrt(100)
    from turtle import * #Don't need the dot ex. forward(10) # * means import everything
        from math import pi #this would only import pi
    import matplotlib as m #Like first example but matplotlib is now m ex. m.plot()
        Intended to be used only for long names
        Usually avoid this one
Don't name your file math.py or turtle.py etc.
Import statements should follow header   They should be the first lines of the actual code
'''
from turtle import *
'''
speed(10)
pensize(5)
pencolor('blue')

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
'''

def draw_poly(color, thickness, nsides, side_length):
    ''' (string, int, int, num) -> None
    Draws a polygon to the turtle window
    >>> draw_poly('blue', 5, 6, 100)
    blue hexagon drawn to turtle window #Or "Creates a Turtle graphic"
    '''
    pencolor(color)
    pensize(thickness)

    for i in range(nsides):
        forward(side_length)
        left(360 / nsides)

    return None

draw_poly('red', 6, 11, 100)
'''
penup
pendown
goto
def move_t(x,y):
    penup()
    goto(x,y)
    pendown()
for i in range(10):
    draw_poly('red', 6, 11, 100)
    move_t(50, -50)
    draw_poly('blue', 2, 4, 200)
'''


