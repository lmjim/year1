'''
Fizzbuzz
CIS 210 F17 Project 1-2

Author: Lily Jim

Credits: N/A

Have python count using the rules of Fizzbuzz
'''

def fb(n):
    '''(int) -> None
    Starting at 1 count to a number n.
    If a number is divisible by 3 say Fizz, by 5 say Buzz, and by both say FizzBuzz.
    When done say Game Over.
    >>> fb(15)
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
    Game Over
    >>> fb(3)
    1
    2
    Fizz
    Game Over
    >>> fb(5)
    1
    2
    Fizz
    4
    Buzz
    Game Over
    '''
    count = 1
    for count in range(1, n + 1):
        if count % 3 == 0 and count % 5 == 0:
            print ('FizzBuzz')
            count = count + 1
        elif count % 3 == 0:
            print ('Fizz')
            count = count + 1
        elif count % 5 == 0:
            print ('Buzz')
            count = count + 1
        else:
            print (count)
    print('Game Over')

    return None
