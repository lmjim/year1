def is_pal(s):
    '''(str) -> bool
    Returns True if s is a palindrome,
    False otherwise
    >>> is_pal('tacocat')
    True
    >>> is_pal('')
    True
    >>> is_pal('hello')
    False
    '''
    while(len(s) > 0):
        if s[0] != s[-1]:
            return False
        s = s[1:-1]
    return True

'''
As soon as you've written something testable, TEST IT
Code smallest bits first

Recursion is a method of solving problems in which the solution to your problem can be
expressed in terms of solutions to SMALLER INSTANCES OF THE SAMMMME PROBLEM

A recursive solution in computing requires 2 things:
1) BASE CASE!!! <-- Trivial, terminating case
2) recursive relationship
---> involving a recursive call to some function

Ex. Fractal Tree
    Image in an image in an image in an image
'''

def fact(x):
    if(x==0):
        return 1
    return x * fact(x-1)


def is_palR(s):
    if(len(s) == 0) or (len(s) ==1):
        return True
    return is_palR(s[1:-1]) and (s[0] == s[-1])
