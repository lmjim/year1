'''
Midterm 2 Code Part
Author: Lily Jim
Code I wrote on midterm 2
'''

def rain(rainli):
    positiveCounter = 0
    sum = 0
    for item in rainli:
        if item >= 0:
            sum += item
            positiveCounter += 1
    if positiveCounter == 0:
        return -999
    mean = sum / positiveCounter
    return mean
