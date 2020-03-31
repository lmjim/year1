'''
a = 10 is an assignment
a is a variable and an expression
8 + 2 is an expression
a string is an expression
a == expression

dir() directory, python built in function
displays name space in current scope when given no arguments
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> x = 8
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'x']
>>> dir(__builtins__)
#content of builtins
>>> import math
>>> dir(math)
#shows what is in math
Python uses double underscore with its own names to avoid collisions

doctest -----> doctest.testmod()
doctest is a module (to import)
testmod is in the doctest module
In docstring it finds >>> and will run the example and see if it is correct
TestResults(failed=0, attempted=7)
regression testing = you are regressively as in looking backwards testing your stuff
doctesting isn't always useful (ex. randomized functions)
it doesn't tell you why it doesn't work
its sensitive to all characters including invisible characters
To call it:
    import doctest
    def ....
    func call
    print(doctest.testmod())
it tests everything from the module that it was called in

assert statements:
(see pictures)
assert condition
    || T/F
    ||
if not condition:
    raise AssertionError
assert statements can be toggled on and off
doesn't give a lot of details
think about error handling
    what happens when you input an unacceptable value?

binary:
decimal numbering system - base ten
    ten unique symbols 0123456789
    4618 ---> 4 * 10 ** 3, 6 * 10 ** 2, 1 * 10 ** 1, 8 * 10 ** 0
binary only has 2 unique symbols: 01
    1101 ----> 1 * 2 ** 3, 1 * 2 ** 2, 0 * 2 ** 1, 1 * 2 ** 0
                8 + 4 + 0 + 1 = 13





