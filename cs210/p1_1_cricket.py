'''
Nature's Thermometer: Cricket Chirps.
CIS 210 F17 Project 1

Author: Lily Jim

Credits: N/A

Determine the temperature based on cricket
chirps. (Farmers Almanac)
'''

def chirps_to_ctemp(ch25):
    '''(int) -> float

    Return celsius temp estimated based on
    number of cricket chirps in a 25 second
    interval (ch25) - divide by 3 and add 4
    to get the celsius temperature.
    
    >>> chirps_to_ctemp(48)
    20.0
    >>> chirps_to_ctemp(93)
    35.0
    >>> chirps_to_ctemp(0)
    4.0
    '''
    ch25 = ch25 / 3
    ch25 = ch25 + 4
    return ch25

def chirps_to_ftemp(ch14):
    '''(int) -> None

    Print fahrenheit temp estimated based on
    number of cricket chirps in a 14 second
    interval (ch14) - add 40. None value is returned.

    >>> chirps_to_ftemp(0)
    The estimated temperature,
    based on 0 chirps in 14 seconds, is
    40 degrees fahrenheit.
    >>> chirps_to_ftemp(50)
    The estimated temperature,
    based on 50 chirps in 14 seconds, is
    90 degrees fahrenheit. 
    '''
    ftemp = ch14 + 40
    print('The estimated temperature, based on ', ch14,
          ' chirps in 14 seconds, is ', ftemp, ' degrees fahrenheit.')
    return None
    

