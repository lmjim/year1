'''
Earthquake Watch
CIS 210 F17 Project 7-2

Author: Lily Jim

Credits: N/A

Determine the number of earthquakes provided in a file and
report the mean, median, and mode of the magnitudes
Also report a frequency table for the data
'''
import p62_data_analysis as p62
import doctest

def equake_readf(fname):
    '''(str) -> list
    Open file with earthquake info
    Create and return list of magnitudes
    >>> equake_readf('equake25f_shortest.txt')
    [2.51, 2.52, 2.54, 2.7, 2.75, 2.77, 2.82, 2.96, 3.38]
    >>> equake_readf('equake50f.txt')
    [5.0, 5.0, 5.1, 5.1, 5.2, 5.2, 5.2, 5.4, 5.6, 5.6, 5.7, 5.9, 6.0]
    >>> equake_readf('equake25f_short.txt')
    [2.51, 2.52, 2.54, 2.6, 2.6, 2.61, 2.7, 2.75, 2.77, 2.8, 2.82, 2.89, 2.96, 3.03, 3.03, 3.3, 3.38, 3.55, 3.9]
    '''
    with open(fname, 'r') as checkf:
        line = checkf.readline()
        magnitudes = []
        for line in checkf:
            values = line.strip().split(',')
            magnitudes.append(float(values[4]))
    magnitudes.sort()
    return magnitudes

def equake_analysis(magnitudes):
    '''(list) -> tuple
    Find and return the mean, median, and mode
    of the earthquake magnitudes as a tuple
    >>> equake_analysis([2.51, 2.52, 2.54, 2.7, 2.75, 2.77, 2.82, 2.96, 3.38])
    (2.772222222222222, 2.75, [2.51, 2.52, 2.54, 2.7, 2.75, 2.77, 2.82, 2.96, 3.38])
    >>> equake_analysis([5.0, 5.0, 5.1, 5.1, 5.2, 5.2, 5.2, 5.4, 5.6, 5.6, 5.7, 5.9, 6.0])
    (5.384615384615385, 5.2, [5.2])
    >>> equake_analysis([2.51, 2.52, 2.54, 2.6, 2.6, 2.61, 2.7, 2.75, 2.77, 2.8, 2.82, 2.89, 2.96, 3.03, 3.03, 3.3, 3.38, 3.55, 3.9])
    (2.908421052631579, 2.8, [2.6, 3.03])
    '''
    mean = p62.mean(magnitudes)
    median = p62.median(magnitudes)
    mode = p62.mode(magnitudes)
    mmm = (mean, median, mode)
    
    return mmm

def equake_report(mmm, magnitudes):
    '''(tuple, list) -> None
    Report the number of earthquakes and the mean, median, and mode of the magnitudes
    Also report a frequency table for the number of occurrences of each item in magnitudes
    Returns None
    >>> equake_report((2.772222222222222, 2.75, [2.51, 2.52, 2.54, 2.7, 2.75, 2.77, 2.82, 2.96, 3.38]),[2.51, 2.52, 2.54, 2.7, 2.75, 2.77, 2.82, 2.96, 3.38])
    For the past 9 earthquakes the following is true:
    <BLANKLINE>
    Mean magnitude is: 2.772222222222222
    Median magnitude is: 2.75
    Mode(s) of magitudes is: [2.51, 2.52, 2.54, 2.7, 2.75, 2.77, 2.82, 2.96, 3.38]
    <BLANKLINE>
    ITEM   FREQUENCY
    2.51   1        
    2.52   1        
    2.54   1        
    2.7    1        
    2.75   1        
    2.77   1        
    2.82   1        
    2.96   1        
    3.38   1        
    >>> equake_report((5.384615384615385, 5.2, [5.2]),[5.0, 5.0, 5.1, 5.1, 5.2, 5.2, 5.2, 5.4, 5.6, 5.6, 5.7, 5.9, 6.0])
    For the past 13 earthquakes the following is true:
    <BLANKLINE>
    Mean magnitude is: 5.384615384615385
    Median magnitude is: 5.2
    Mode(s) of magitudes is: [5.2]
    <BLANKLINE>
    ITEM   FREQUENCY
    5.0    2        
    5.1    2        
    5.2    3        
    5.4    1        
    5.6    2        
    5.7    1        
    5.9    1        
    6.0    1        
    >>> equake_report((2.908421052631579, 2.8, [2.6, 3.03]),[2.51, 2.52, 2.54, 2.6, 2.6, 2.61, 2.7, 2.75, 2.77, 2.8, 2.82, 2.89, 2.96, 3.03, 3.03, 3.3, 3.38, 3.55, 3.9])
    For the past 19 earthquakes the following is true:
    <BLANKLINE>
    Mean magnitude is: 2.908421052631579
    Median magnitude is: 2.8
    Mode(s) of magitudes is: [2.6, 3.03]
    <BLANKLINE>
    ITEM   FREQUENCY
    2.51   1        
    2.52   1        
    2.54   1        
    2.6    2        
    2.61   1        
    2.7    1        
    2.75   1        
    2.77   1        
    2.8    1        
    2.82   1        
    2.89   1        
    2.96   1        
    3.03   2        
    3.3    1        
    3.38   1        
    3.55   1        
    3.9    1        
    '''
    print('For the past {} earthquakes the following is true:'.format(len(magnitudes)))
    print('')
    print('Mean magnitude is: {}'.format(mmm[0]))
    print('Median magnitude is: {}'.format(mmm[1]))
    print('Mode(s) of magitudes is: {}'.format(mmm[2]))
    print('')
    magnitude_freq = p62.freqTable(magnitudes)
    return None

def main():
    '''() -> None
    Calls equake_readf, equake_analysis, and equake_report
    Top level function for earthquake data analysis
    Returns None
    '''
    #fname = 'equake25f_shortest.txt'
    #fname = 'equake50f.txt'
    #fname = 'equake25f_short.txt'
    fname = 'equake25f.txt'

    magnitudes = equake_readf(fname)
    mmm = equake_analysis(magnitudes)
    equake_report(mmm, magnitudes)
    
    return None

if __name__ == '__main__':
    #print(doctest.testmod())
    main()

