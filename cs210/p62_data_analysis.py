"""
CIS210 Project 6-2 Fall 2017 

Author: [Solution]

Credits: N/A

Implement functions from text ch. 4 -
mean, median, mode, frequency table,
visualization (chart and table) -
with some revisions.

Practice:
-- lists
-- dictionaries
-- basic data processing
"""

import doctest
import statistics
#from turtle import *

def mean(alist):
    '''(list of numbers) -> number

    Return mean of alist (len > 0).

    >>> mean([3, 1, 2])
    2.0
    >>> mean([0, 0])
    0.0
    >>> mean([99])
    99.0
    '''
    mean = sum(alist) / len(alist)
    return mean

def isEven(n):
    '''(num) -> boolean

    Return True if n is even,
    else return False

    >>> even(4)
    True
    >>> even(1)
    False
    >>> even(0)
    True
    '''
    return (n % 2) == 0

def median(alist):
    '''(list of numbers) -> number

    Return median of alist (of len > 0).

    >>> median([5, 7, 1, 3])
    4.0
    >>> median([1, 2, 2, 3, 99])
    2
    >>> median([99]) 
    99
    >>> median([0, 0, 0, 0]) 
    0.0
    '''
    copyl = alist[:]
    copyl.sort()
    copylen = len(copyl)
    
    if isEven(copylen):
        rmid = copylen // 2
        lmid = rmid - 1
        medi = (copyl[lmid] + copyl[rmid]) / 2
    else:
        mid = copylen // 2
        medi = copyl[mid]

    return medi

def mode(alist):
    '''(list of numbers) -> list

    Return mode(s) of alist.

    Calls: genFreqTable

    >>> mode([5, 7, 1, 3])  
    [1, 3, 5, 7]
    >>> mode([1, 2, 2, 3, 99])
    [2]
    >>> mode([99]) 
    [99]
    >>> mode([0, 0, 1, 1])  
    [0, 1]
    '''
    countd = genFreqTable(alist)

    countli = countd.values()
    maxct = max(countli)

    #there may be more than one mode
    modeli = []
    for k in countd:
        if countd[k] == maxct:
            modeli.append(k)
    '''
    modeli = [k for k in countd if countd[k] == maxct]
    '''   
    return modeli

def genFreqTable(alist):
    '''(list of numbers) -> dictionary

    Generate a frequency dictionary with
    number of occurrences of each number
    in alist.

    Called by:  freqTable, freqChart, mode

    > genFreqTable([1, 2, 3, 3, 1, 4, 5])
    {1:2, 2:1, 3:2, 4:1, 5:1}
    '''
    freqD = {}
    '''
    for item in alist:
        if item in freqD:
            freqD[item] += 1
        else:
            freqD[item] = 1
    '''
    # better - use dict set default method
    for item in alist:
        freqD.setdefault(item, 0)
        freqD[item] += 1

    return freqD


def freqTable(alist):
    '''(list of numbers) -> None

    Print frequency table of count
    of each number in alist.
    None value is returned.

    Calls:  genFreqTable, drawTable

    > freqTable([1, 2, 3, 3, 1, 4, 5])
    [frequency occurrences chart] 
    '''
    freqD = genFreqTable(alist)
    drawTable(freqD)
 
    return None

def drawTable(freqD):
    '''(dict) -> None

    Display each key-value pair
    from freqD in a frequency table.
    None value is returned.
   
    Called by: freqTable

    >>> drawTable({1:2, 2:1, 3:2, 4:1, 5:1})
    ITEM  FREQUENCY
    1     2
    2     1
    3     2
    4     1
    5     1
    '''
    iteml = list(freqD)
    iteml.sort()
    #iteml.sort(reverse=True)

    #could use sorted function instead
    #iteml = sorted(freqD)
    #or, to sort by value 
    #iteml = sorted(freqD, key=freqD.__getitem__, reverse=True)

    print('{: <6} {: <9}'.format('ITEM', 'FREQUENCY'))

    for item in iteml:
        print('{: <6} {: <9}'.format(item, freqD[item]))

    return None

def freqChart(alist):
    '''(list of numbers) -> None

    Draw frequency chart of count
    of each number in alist.
    None value is returned.

    Calls:  genFreqTable, drawChart

    > freqChart([1, 2, 3, 3, 1, 4, 5])
    [frequency occurrences chart] 
    '''
    freqD = genFreqTable(alist)
    drawChart(freqD)
        
    return None

def drawChart(freqD):
    '''(dictionary of items/number occurrences) -> None
    
    Draw frequency chart of
    items and frequency count in freqD.
    None value is returned.

    Called by: freqChart

    > drawChart(6, 10)
    [frequency chart]
    '''
    # find min and max items
    # for drawing graph outline
    iteml = list(freqD.keys())
    iteml.sort()
    minitem = 0
    maxitem = len(iteml) - 1

    # do the same for occurrence values
    countl = freqD.values()
    maxcount = max(countl)

    # use these numbers to scale
    # the canvas appropriately
    wn = Screen()
    setworldcoordinates(-1, -1, maxitem+1, maxcount+1)

    # set up the turtle
    hideturtle()
    speed('fastest')

    # draw the chart outlines
    penup()
    goto(0,0)
    pendown()
    goto(maxitem, 0)
    penup()

    goto(-1, 0)
    write('0', font=('Helvetica', 16, 'bold'))
    goto(-1, maxcount)
    write(str(maxcount), font=('Helvetica', 16, 'bold'))

    #label the x-axis
    for i in range(len(iteml)):
        goto(i, -1)
        write(str(iteml[i]), font=('Helvetica', 16, 'bold'))

    #graph the number of occurrences
        goto(i, 0)
        pendown()
        goto(i, freqD[iteml[i]])
        penup()

    #wn.exitonclick()
    return None

shortlist = [1, 2, 3, 1, 2, 2, 2, 4, 1]

equakes = [5.3, 3.0, 2.6, 4.4, 2.9, 4.8, 4.3,
           2.6, 2.9, 4.9, 2.5, 4.8, 4.2, 2.6,
           4.8, 2.7, 5.0, 2.7, 2.8, 4.3, 3.1,
           4.1, 2.8, 5.8, 2.5, 3.9, 4.8, 2.9,
           2.5, 4.9, 5.0, 2.5, 3.2, 2.6, 2.7,
           4.8, 4.1, 5.1, 4.7, 2.6, 2.9, 2.7,
           3.3, 3.0, 4.4, 2.7, 5.7, 2.5, 5.1,
           2.5, 4.4, 4.6, 5.7, 4.5, 4.7, 5.1,
           2.9, 3.3, 2.7, 2.8, 2.9, 2.6, 5.3,
           6.0, 3.0, 5.3, 2.7, 4.3, 5.4, 4.4,
           2.6, 2.8, 4.4, 4.3, 4.7, 3.3, 4.0,
           2.5, 4.9, 4.9, 2.5, 4.8, 3.1, 4.9,
           4.4, 6.6, 3.3, 2.5, 5.0, 4.8, 2.5,
           4.2, 4.5, 2.6, 4.0, 3.3, 3.1, 2.6,
           2.7, 2.9, 2.7, 2.9, 3.3, 2.8, 3.1,
           2.5, 4.3, 3.2, 4.6, 2.8, 4.8, 5.1,
           2.7, 2.6, 3.1, 2.9, 4.2, 4.8, 2.5,
           4.5, 4.5, 2.8, 4.7, 4.6, 4.6, 5.1,
           4.2, 2.8, 2.5, 4.5, 4.6, 2.6, 5.0,
           2.8, 2.9, 2.7, 3.1, 2.6, 2.5, 3.2,
           3.2, 5.2, 2.8, 3.2, 2.6, 5.3, 5.5,
           2.7, 5.2, 6.4, 4.2, 3.1, 2.8, 4.5,
           2.9, 3.1, 4.3, 4.9, 5.2, 2.6, 6.7,
           2.7, 4.9, 3.0, 4.9, 4.7, 2.6, 4.6,
           2.5, 3.2, 2.7, 6.2, 4.0, 4.6, 4.9,
           2.5, 5.1, 3.3, 2.5, 4.7, 2.5, 4.1,
           3.1, 4.6, 2.8, 3.1, 6.3]

def main():
    '''controller for earthquake data funcs '''
    freqTable(equakes)
    #freqChart(equakes)
    print()
    print('Mean value is:', mean(equakes))
    print('Python mean is:', statistics.mean(equakes))
    print()
    print('Median value is:', median(equakes))
    print('Python median is:', statistics.median(equakes))
    print()
    print('Mode is:', mode(equakes))
    print('Python mode is:', statistics.mode(equakes))

    return None

if __name__ == '__main__':
    main()


#print(doctest.testmod())

          
    
    

    

    
    
