''' 
CIS 210 STYLE
CIS 210 F17 Project 1

Author: Lily Jim

Credits: N/A

Add docstrings to Python functions implementing quiz 1 pseudocode.
'''

def q1(onTime, absent):
    '''(Boolean, Boolean) -> None
    Returns appropriate phrase based on if someone was on time, late, or absent.
    Does not recognize that one cannot be on time and absent.
    >>> q1(True, False)
    Hello!
    >>> q1(False, False)
    Better late than never.
    >>> q1(False, True)
    Is anyone there?
    '''
    if onTime:
        print('Hello!')
    elif absent:
        print('Is anyone there?')
    else:
        print('Better late than never.')

    return None


def q2(age, salary):
    '''(int, int) -> Boolean
    Returns False if age is not less than 18 or salary is not less than 10000.
    Returns True if both age and salary are equal to or more than 18 and 10000 respectively.
    >>> q2(18, 12000)
    False
    >>> q2(15, 8000)
    True
    >>> q2(12, 15000)
    False
    >>> q2(20, 2000)
    False
    '''
    return (age < 18) and (salary < 10000)


def q3():
    '''() -> int
    Returns result based off of given values of p and q
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


def q4(balance, deposit):
    '''(int, int) -> int
    Returns the final balance after the deposit is added to the initial balance 10 times.
    >>> q4(12, 15)
    162
    >>> q4(500, 10)
    600
    '''
    count = 0
    while count < 10:
        balance = balance + deposit
        count += 1

    return balance


def q5(nums):
    '''([list]) -> int
    Return the number of non-negative integers given.
    >>> q5([16,22,56,71,8])
    5
    >>> q5([12,6])
    2
    >>> q5([8, -7, 5, 20, -2, -9])
    3
    '''
    result = 0
    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            result += 1

        i += 1

    return result


def q6():
    '''() -> None
    Multiplies p by 2 while adding 1 to i until i is 4
    returning a string related to the value of p.
    >>> q6()
    2-power is 16
    '''
    i = 0
    p = 1
    while i < 4:
        #i = 1 Causes infinite loop
        p = p * 2
        i += 1

    print('2-power is', p)
    
    return None




    
