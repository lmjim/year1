'''
Who is in this class?
CIS 210 F17 Project 7-1

Author: Lily Jim

Credits: N/A

Determine the major with the most students in CIS210
Report a frequency table with the number of times a
major appears within the class
'''
import p62_data_analysis as p62
import doctest

def majors_readf(fname):
    ''' (str) -> list
    Open file with class info
    Create and return list of majors
    >>> majors_readf('majors_short.txt')
    ['CIS', 'CIS', 'EC', 'GSS', 'PBA', 'PS', 'SDSC']
    >>> majors_readf('majors_random_ex.txt')
    ['CIS', 'CIS', 'CIS', 'CIS', 'EC', 'GSS', 'J', 'J', 'J', 'J', 'PBA', 'PS', 'SDSC', 'UNDL', 'UNDL', 'UNDL', 'UNDL']
    >>> majors_readf('majors_cis210f17.txt')
    ['ACTG', 'ATCH', 'ATCH', 'BI', 'BI', 'BI', 'BI', 'CEP', 'CEP', 'CH', 'CH', 'CH', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'EC', 'EC', 'EC', 'EC', 'EC', 'EC', 'ERTH', 'GEOG', 'GEOG', 'GS', 'GSS', 'GSS', 'HPHY', 'J', 'MACS', 'MACS', 'MACS', 'MACS', 'MACS', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MUS', 'MUS', 'PBA', 'PBA', 'PBA', 'PBA', 'PBA', 'PBA', 'PBA', 'PDS', 'PEN', 'PEN', 'PEN', 'PHYS', 'PHYS', 'PHYS', 'PHYS', 'PHYS', 'PS', 'PS', 'PS', 'PSY', 'PSY', 'SDSC', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL']
    '''
    with open(fname, 'r') as checkf:
        line = checkf.readline() #Skip header
        majorsli = []
        for line in checkf:
            values = line.strip().split()
            majorsli.append(values[0]) #Add the major and not department to the list
            
    majorsli.sort() #Group each major together and present alphabetically for easier reading
    
    return majorsli

def majors_analysis(majorsli):
    ''' (list) -> str
    Find and return the mode of a list of majors
    >>> majors_analysis(['CIS', 'CIS', 'EC', 'GSS', 'PBA', 'PS', 'SDSC'])
    'CIS'
    >>> majors_analysis(['CIS', 'CIS', 'CIS', 'CIS', 'EC', 'GSS', 'J', 'J', 'J', 'J', 'PBA', 'PS', 'SDSC', 'UNDL', 'UNDL', 'UNDL', 'UNDL'])
    'CIS, J, UNDL'
    >>> majors_analysis(['ACTG', 'ATCH', 'ATCH', 'BI', 'BI', 'BI', 'BI', 'CEP', 'CEP', 'CH', 'CH', 'CH', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'EC', 'EC', 'EC', 'EC', 'EC', 'EC', 'ERTH', 'GEOG', 'GEOG', 'GS', 'GSS', 'GSS', 'HPHY', 'J', 'MACS', 'MACS', 'MACS', 'MACS', 'MACS', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MUS', 'MUS', 'PBA', 'PBA', 'PBA', 'PBA', 'PBA', 'PBA', 'PBA', 'PDS', 'PEN', 'PEN', 'PEN', 'PHYS', 'PHYS', 'PHYS', 'PHYS', 'PHYS', 'PS', 'PS', 'PS', 'PSY', 'PSY', 'SDSC', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL'])
    'CIS'
    '''
    mode_list = p62.mode(majorsli)
    
    #Present mode as a string and not list:
    if len(mode_list) > 1: #When the mode is more than one major add commas between majors
        majors_mode = ''
        for item in mode_list:
            majors_mode += item
            if item != mode_list[-1]:
                majors_mode += ', '
    else:
        majors_mode = mode_list[0]
    
    return majors_mode

def majors_report(majors_mode, majorsli):
    ''' (str, list) -> None
    Report the mode and a frequency table for a list of majors
    Returns None
    >>> majors_report('CIS', ['CIS', 'CIS', 'EC', 'GSS', 'PBA', 'PS', 'SDSC'])
    Most represented major(s):
    CIS
    <BLANKLINE>
    ITEM   FREQUENCY
    CIS    2        
    EC     1        
    GSS    1        
    PBA    1        
    PS     1        
    SDSC   1        
    >>> majors_report('CIS, J, UNDL', ['CIS', 'CIS', 'CIS', 'CIS', 'EC', 'GSS', 'J', 'J', 'J', 'J', 'PBA', 'PS', 'SDSC', 'UNDL', 'UNDL', 'UNDL', 'UNDL'])
    Most represented major(s):
    CIS, J, UNDL
    <BLANKLINE>
    ITEM   FREQUENCY
    CIS    4        
    EC     1        
    GSS    1        
    J      4        
    PBA    1        
    PS     1        
    SDSC   1        
    UNDL   4        
    >>> majors_report('CIS', ['ACTG', 'ATCH', 'ATCH', 'BI', 'BI', 'BI', 'BI', 'CEP', 'CEP', 'CH', 'CH', 'CH', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'EC', 'EC', 'EC', 'EC', 'EC', 'EC', 'ERTH', 'GEOG', 'GEOG', 'GS', 'GSS', 'GSS', 'HPHY', 'J', 'MACS', 'MACS', 'MACS', 'MACS', 'MACS', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MATH', 'MUS', 'MUS', 'PBA', 'PBA', 'PBA', 'PBA', 'PBA', 'PBA', 'PBA', 'PDS', 'PEN', 'PEN', 'PEN', 'PHYS', 'PHYS', 'PHYS', 'PHYS', 'PHYS', 'PS', 'PS', 'PS', 'PSY', 'PSY', 'SDSC', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL', 'UNDL'])
    Most represented major(s):
    CIS
    <BLANKLINE>
    ITEM   FREQUENCY
    ACTG   1        
    ATCH   2        
    BI     4        
    CEP    2        
    CH     3        
    CIS    78       
    EC     6        
    ERTH   1        
    GEOG   2        
    GS     1        
    GSS    2        
    HPHY   1        
    J      1        
    MACS   5        
    MATH   15       
    MUS    2        
    PBA    7        
    PDS    1        
    PEN    3        
    PHYS   5        
    PS     3        
    PSY    2        
    SDSC   1        
    UNDL   26       
    '''
    print('Most represented major(s):')
    print(majors_mode)
    print('')
    major_freq = p62.freqTable(majorsli)
    return None

def main():
    ''' () -> None
    Calls majors_readf, majors_analysis, and majors_report
    Top level functoin for analysis of CIS 210 majors data
    Returns None
    '''
    #fname = 'majors_short.txt'
    #fname = 'majors_random_ex.txt'
    fname = 'majors_cis210f17.txt'
    
    majorsli = majors_readf(fname)
    majors_mode = majors_analysis(majorsli)
    majors_report(majors_mode, majorsli)

    return None

if __name__ == '__main__':
    #print(doctest.testmod())
    main()

