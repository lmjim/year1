'''
Data from the web, Part 1
CIS 210 F17 Project 9-1

Author: Lily Jim

Credits: TODO

TODO
'''
import urllib.request
import p8f_equakes_vis as p8


def readeqf(fname):
    '''(str) -> TODO
    TODO
    >>> TODO
    TODO
    >>> readeqf('http://earthquake.usgs.gov/fdsnws/event/1/\
    query?format=csv\
    &starttime=1916-11-01\
    &latitude=44.052071\
    &longitude=-123.086754\
    &maxradiuskm=250\
    &minmagnitude=5')
    TODO
    '''
    with urllib.request.urlopen(fname) as info:
        #for line in info:
        ftext = info.readline()
        ftext = ftext.decode().strip()
        print(ftext)
    
    return None

