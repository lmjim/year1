'''
Other IDEs are:
Jupiter Notebook
PyCharm
Eclipse
IDLE
Sublime Text - Text editor

import random
def roll_dice():

    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    print(roll1, '', '', roll2)
    return None

for i in range(30):
    roll_dice()


Why functions?
1. reuseablility
2. modularity
3. readability

Company:      Size:  Price:
Falling Sky   14     19
Falling Sky   18     27
Pegasus       10     13
Pegasus       14     19
Pegasus       16     24
Dominoes      14     16
Dominoes      16     18


Given a diameter and cost, print (return??) the
price per square inch of the pizza
'''
import math

def pizza_calc(diameter, cost):
    '''(num, num) -> float
    Given a diameter and cost, finds and reports the price
    per square inch of pizza.
    >>> pizza_calc(14, 19)
    Price per square inch: $0.12
    '''
    #Find pizza area
    r = diameter / 2
    area = math.pi * (r ** 2)
    #Or make another definition and use area = get_area(diameter)
    #Divide cost by area
    price_per_sqin = cost / area
    rounded_price = round(price_per_sqin, 2)
    #Print Result
    print('Price per square inch: $', rounded_price, sep='')
    #If we want to use the result of this function somewhere else,
    #then we want to return the value (but not in this case)
    #Return None
    
    return None


def get_area(diameter):
    '''(num) -> float
    Finds and returns area of circle with given diameter
    >>> get_area(1)
    3.14
    '''
    r = diameter / 2
    area = math.pi * (r ** 2)
    return area

pizza_calc(14, 19)





'''
def find_best_deal(list_of_pizza_info):
    #This would want pizza_calc to return a value
    pizza1_val = pizza_calc(p1_d, p1_c)
'''






