'''
Examples of Docstrings
From CIS 210 F17 Project 1 Solutions
'''
''' 
CIS 210 Style
CIS 210 F17 Project 1

Author: Solution

Credits: N/A

Add docstrings to Python functions implementing quiz 1 pseudocode.
'''
import doctest

def q1(onTime, absent):
    '''
    (Boolean, Boolean) -> None

    Print appropriate messages responding to ontime,
    late, or missing.

    >>> q1(True, True)
    Hello!
    >>> q1(False, True)
    Is anyone there?
    >>> q1(False, False)
    Better late than never.
    '''    
    if onTime:
        print('Hello!')
    elif absent:
        print('Is anyone there?')
    else:
        print('Better late than never.')

    return None

#q1(False, False)

def q2(age, salary):
    '''
    (number, number) -> Boolean

    Return True if conditions for tax dependent
    are met (age under 18, salary less than $10K).

    >>> q2(18, 5000)
    False
    >>> q2(16, 5000)
    True
    '''
    return (age < 18) and (salary < 10000)

#print(q2(18, 5000))
#print(q2(16, 5000))

def q3():
    '''
    () -> integer

    Example exercise, conditional and Booleans.

    >>> q3()
    6
    '''
    p = 1
    q = 2
    result = 4
    if p < q:
        if q > 4:
            result = 5
        else:
            result = 6

    return result

#print(q3())

def q4(balance, deposit):
    '''
    (number, number) -> number

    Add deposit for 10 intervals to
    initial balance; return new balance.

    >>> q4(100, 10)
    200
    >>> q4(0, 100)
    1000
    '''
    count = 0
    while count < 10:
        balance = balance + deposit
        count += 1

    return balance

#print(q4(100, 10))

def q5(nums):
    '''
    (list of numbers) -> integer

    Return count of non-negative numbers
    in list nums.

    >>> q5([0, 1, 2, 3, 4, 5])
    6
    >>> q5([0, -1, 2, -3, 4, -5])
    3
    '''
    result = 0
    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            result += 1

        i += 1

    return result

#print(q5([0, 1, 2, 3, 4, 5]))
#print(q5([0, -1, 2, -3, 4, -5]))

def q6():
    '''
    () -> None

    Print 2 to the power of 4.
    (Fixed bug that was on the quiz.)

    >>> q6()
    2-power is 16
    '''
    i = 0
    p = 1
    while i < 4:
        # i = 1
        p = p * 2
        i += 1

    print('2-power is', p)
    return None

#q6()

def q6_better():
    '''
    () -> None

    Print 2 to the power of 4.
    (Fixed bug that was on the quiz.)

    >>> q6_better()
    2-power is 16
    '''
    p = 1
    for i in range(4):
        p = p * 2

    print('2-power is', p)
    return None

#q6_better()
