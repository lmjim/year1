"""
CIS210 Project 6-1 Fall 2017 

Author: [Solution]

Credits: N/A

Implement a function to test the string 
reverse functions from project 5
(iterative and recursive).

Practice:
-- user-defined test functions
-- functions as parameters
"""

import p52_stringreverse_key as p5
        
def test_reverse(f):
    '''(function) -> None

    Test function f (one of the
    string reverse functions).
    Report results for each test.

    > test_reverse(p5.strReverseR)
    <report results>
    > test_reverse(p5.strReverseI)
    <report results>				
    '''
    test_cases = (
        ('', ''),
        ('a', 'b'),
        ('xyz', 'zyx'),
        ('testing123', '321gnitset'),
        ('hello, world', 'dlrow ,olleh')
        )
    
    for test in test_cases:
        # parse the arguments
        arg1 = test[0]
        expected_result = test[1]

        # report test case
        print('Checking {}({}) ...'.format(
            f.__name__, str(arg1)), end='')

        # execute the test
        actual_result = f(arg1)

        # report result
        if (actual_result == expected_result):
            print('its value {} is correct!'.format(actual_result))
        else:
            print('Error: has wrong value {}, expected {}.'.format(actual_result,
                                                                   expected_result))
    return None

def main():
    '''calls string reverse test func 2x'''
    test_reverse(p5.strReverseR)   
    test_reverse(p5.strReverseI)

    return None

if __name__ == '__main__':
    #print(doctest.testmod())
    main()

    
    
