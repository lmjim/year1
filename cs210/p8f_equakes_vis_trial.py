'''
World-wide Earthquake Watch
CIS 210 F17 Project 8

Author: Lily Jim

Credits: Based on code in ch.7 of Miller and Ranum text

Map out earthquake clusters using Turtle
'''
import math
import random
import turtle

def readFile(filename):
    '''(str) -> dictionary
    Open file with earthquake data
    Create and return a dictionary of lists that
    contain longitude and latitude points
    >>> readFile('earthquakes_shortest.txt')
    {1: [129.2695, 36.0645], 2: [-174.6136, -17.4576], 3: [-17.1484, -59.0385], 4: [154.4975, -6.1003], 5: [143.7091, 13.0671]}
    >>> readFile('earthquakes_shorter.txt')
    {1: [129.2695, 36.0645], 2: [-174.6136, -17.4576], 3: [-17.1484, -59.0385], 4: [154.4975, -6.1003], 5: [143.7091, 13.0671], 6: [70.8258, -26.1652], 7: [-177.8336, -31.7723], 8: [-171.6991, -18.9217], 9: [-177.3966, -31.2848], 10: [-177.9864, -18.1544]}
    >>> readFile('earthquakes_short.txt')
    {1: [129.2695, 36.0645], 2: [-174.6136, -17.4576], 3: [-17.1484, -59.0385], 4: [154.4975, -6.1003], 5: [143.7091, 13.0671], 6: [70.8258, -26.1652], 7: [-177.8336, -31.7723], 8: [-171.6991, -18.9217], 9: [-177.3966, -31.2848], 10: [-177.9864, -18.1544], 11: [168.7883, -21.6469], 12: [145.4688, -3.489], 13: [-84.5054, 9.5264], 14: [144.8897, 38.0555], 15: [45.5993, 34.9144]}
    '''
    datafile = open(filename, 'r')
    datadict = {}
    key = 0
    aline = datafile.readline() #move past headers
    for aline in datafile:
        items = aline.split(',') #split on commas
        key = key + 1
        lat = float(items[1]) #latitude is in spot 1
        lon = float(items[2]) #longitude is in spot 2
        datadict[key] = [lon, lat]
    return datadict

def euclidD(point1, point2):
    '''(list, list) -> float
    Return the distance between two locations
    >>> euclidD([129.2695, 36.0645],[-174.6136, -17.4576])
    308.5604538077101
    >>> euclidD([129.2695, 36.0645],[-177.9864, -18.1544])
    312.0030083220673
    >>> euclidD([129.2695, 36.0645],[45.5993, 34.9144])
    83.67810405386822
    '''
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total = total + diff
    euclidDistance = math.sqrt(total)
    return euclidDistance

def createCentroids(k, datadict):
    '''(int, dict) -> list
    Finds center points, or centroids, for the number of clusters wanted
    Centroids appear as a list [longitude, latitude]
    Returns a list of centroids
    Note: due to randomness, centroids may vary each time the function executes
    >>> createCentroids(3, {1: [129.2695, 36.0645], 2: [-174.6136, -17.4576], 3: [-17.1484, -59.0385], 4: [154.4975, -6.1003], 5: [143.7091, 13.0671]})
    [[129.2695, 36.0645], [143.7091, 13.0671], [154.4975, -6.1003]]
    >>> createCentroids(5, {1: [129.2695, 36.0645], 2: [-174.6136, -17.4576], 3: [-17.1484, -59.0385], 4: [154.4975, -6.1003], 5: [143.7091, 13.0671]})
    [[154.4975, -6.1003], [143.7091, 13.0671], [129.2695, 36.0645], [-174.6136, -17.4576], [-17.1484, -59.0385]]
    >>> createCentroids(3, {1: [129.2695, 36.0645], 2: [-174.6136, -17.4576], 3: [-17.1484, -59.0385], 4: [154.4975, -6.1003], 5: [143.7091, 13.0671], 6: [70.8258, -26.1652], 7: [-177.8336, -31.7723], 8: [-171.6991, -18.9217], 9: [-177.3966, -31.2848], 10: [-177.9864, -18.1544]})
    [[143.7091, 13.0671], [-177.3966, -31.2848], [129.2695, 36.0645]]
    '''
    centroids = []
    centroidCount = 0
    centroidKeys = []
    while centroidCount < k:
        rkey = random.randint(1, len(datadict))
        if rkey not in centroidKeys:
            centroids.append(datadict[rkey])
            centroidKeys.append(rkey)
            centroidCount = centroidCount + 1
    return centroids

def createClusters(k, centroids, datadict, repeats):
    '''(int, list, dict, int) -> list
    Determines which earthquakes are nearest which centroids
    Creates lists of which earthquakes are a part of which clusters
    using the earthquakes' dictionary key
    Returns a list of clusters containing which earthquakes are in the cluster
    >>> createClusters(3, [[129.2695, 36.0645], [143.7091, 13.0671], [154.4975, -6.1003]], {1: [129.2695, 36.0645], 2: [-174.6136, -17.4576], 3: [-17.1484, -59.0385], 4: [154.4975, -6.1003], 5: [143.7091, 13.0671]}, 1)
    [[1, 2, 3], [5], [4]]
    >>> createClusters(3, [[129.2695, 36.0645], [143.7091, 13.0671], [154.4975, -6.1003]], {1: [129.2695, 36.0645], 2: [-174.6136, -17.4576], 3: [-17.1484, -59.0385], 4: [154.4975, -6.1003], 5: [143.7091, 13.0671]}, 5)
    [[2, 3], [1, 5], [4]]
    >>> createClusters(3, [[143.7091, 13.0671], [-177.3966, -31.2848], [129.2695, 36.0645]], {1: [129.2695, 36.0645], 2: [-174.6136, -17.4576], 3: [-17.1484, -59.0385], 4: [154.4975, -6.1003], 5: [143.7091, 13.0671], 6: [70.8258, -26.1652], 7: [-177.8336, -31.7723], 8: [-171.6991, -18.9217], 9: [-177.3966, -31.2848], 10: [-177.9864, -18.1544], 11: [168.7883, -21.6469], 12: [145.4688, -3.489], 13: [-84.5054, 9.5264], 14: [144.8897, 38.0555], 15: [45.5993, 34.9144]}, 5)
    [[4, 5, 6, 11, 12], [2, 3, 7, 8, 9, 10, 13], [1, 14, 15]]
    '''
    for apass in range(repeats):
        #print('**** PASS', apass, '****')
        clusters = []
        for i in range(k):
            clusters.append([])
        for akey in datadict:
            distances = []
            for clusterIndex in range(k):
                dist = euclidD(datadict[akey], centroids[clusterIndex])
                distances.append(dist)
            mindist = min(distances)
            index = distances.index(mindist)
            clusters[index].append(akey)
        dimensions = len(datadict[1])
        for clusterIndex in range(k): 
            sums = [0] * dimensions
            for akey in clusters[clusterIndex]:
                datapoints = datadict[akey]
                for ind in range(len(datapoints)):
                    sums[ind] += datapoints[ind]
            for ind in range(len(sums)):
                clusterLen = len(clusters[clusterIndex])
                if clusterLen != 0:
                    sums[ind] = sums[ind]/clusterLen
            centroids[clusterIndex] = sums
        '''for c in clusters:
            print('CLUSTER')
            for key in c:
                print(datadict[key], end=' ')
            print()'''
    return clusters

def eqDraw(k, eqDict, eqClusters):
    '''(int, dict, list) -> None
    Plots each earthquake location on a map in Turtle
    Each dot is color coated to show which cluster it is apart of
    Note: k cannot exceed 6
    >>> eqDraw(3,{1: [129.2695, 36.0645], 2: [-174.6136, -17.4576], 3: [-17.1484, -59.0385], 4: [154.4975, -6.1003], 5: [143.7091, 13.0671], 6: [70.8258, -26.1652], 7: [-177.8336, -31.7723], 8: [-171.6991, -18.9217], 9: [-177.3966, -31.2848], 10: [-177.9864, -18.1544], 11: [168.7883, -21.6469], 12: [145.4688, -3.489], 13: [-84.5054, 9.5264], 14: [144.8897, 38.0555], 15: [45.5993, 34.9144]},[[3, 13], [2, 7, 8, 9, 10], [1, 4, 5, 6, 11, 12, 14, 15]])
    #Each earthquake location is plotted, 3 colors are used to show 3 large clusters
    >>> eqDraw(6,{1: [129.2695, 36.0645], 2: [-174.6136, -17.4576], 3: [-17.1484, -59.0385], 4: [154.4975, -6.1003], 5: [143.7091, 13.0671], 6: [70.8258, -26.1652], 7: [-177.8336, -31.7723], 8: [-171.6991, -18.9217], 9: [-177.3966, -31.2848], 10: [-177.9864, -18.1544], 11: [168.7883, -21.6469], 12: [145.4688, -3.489], 13: [-84.5054, 9.5264], 14: [144.8897, 38.0555], 15: [45.5993, 34.9144]},[[1, 14], [4, 5, 11, 12], [7, 9], [3, 6, 15], [13], [2, 8, 10]])
    #Each earthquake location is plotted, 6 colors are used to show 6 oddly shaped clusters
    >>> eqDraw(6,{1: [129.2695, 36.0645], 2: [-174.6136, -17.4576], 3: [-17.1484, -59.0385], 4: [154.4975, -6.1003], 5: [143.7091, 13.0671], 6: [70.8258, -26.1652], 7: [-177.8336, -31.7723], 8: [-171.6991, -18.9217], 9: [-177.3966, -31.2848], 10: [-177.9864, -18.1544], 11: [168.7883, -21.6469], 12: [145.4688, -3.489], 13: [-84.5054, 9.5264], 14: [144.8897, 38.0555], 15: [45.5993, 34.9144]},[[4, 11], [13], [3, 6, 15], [2, 7, 8, 9, 10], [5, 12], [1, 14]])
    #Each earthquake location is plotted, 6 colors are used to show 6 fairly concise clusters
    '''
    quakeT = turtle.Turtle()
    quakeWin = turtle.Screen()
    quakeWin.bgpic('worldmap.gif')
    quakeWin.screensize(1800, 900) #Set map size
    quakeWin.setup(width = 1850, height = 950) #Set window large enough to see entire map

    wFactor = (quakeWin.screensize()[0]/2)/180
    hFactor = (quakeWin.screensize()[1]/2)/90

    quakeT.hideturtle()
    quakeT.up()
    quakeT.speed('fastest') #Speed up placement of dots

    colorlist = ['red', 'green', 'blue', 'orange', 'cyan', 'yellow'] #Only 6 colors in list so k <= 6

    for clusterIndex in range(k):
        quakeT.color(colorlist[clusterIndex])
        for akey in eqClusters[clusterIndex]:
            lon = eqDict[akey][0]
            lat = eqDict[akey][1]
            quakeT.goto(lon * wFactor, lat * hFactor)
            quakeT.dot()
    quakeWin.exitonclick()
    return None

def visualizeQuakes(k, dataFile, r):
    '''(int, str, int) -> None
    Calls readFile, createCentroids, createClusters, and eqDraw
    Returns None
    Note: due to randomness in createCentroids results may differ
    Note: due to eqDraw, k should not exceed 6
    >>> visualizeQuakes(3, 'earthquakes.txt', 7)
    #Each earthquake location is plotted, 3 colors are used to show 3 large clusters
    >>> visualizeQuakes(6, 'earthquakes.txt', 3)
    #Each earthquake location is plotted, 6 colors are used to show 6 oddly shaped clusters
    >>> visualizeQuakes(6, 'earthquakes.txt', 7)
    #Each earthquake location is plotted, 6 colors are used to show 6 fairly concise clusters
    '''
    datadict = readFile(dataFile)
    quakeCentroids = createCentroids(k, datadict)
    clusters = createClusters(k, quakeCentroids, datadict, r)
    eqDraw(k, datadict, clusters)
    return None


def main():
    '''() -> None
    Calls visualizeQuakes
    Top level function for visualize earthquakes
    Returns None
    '''
    visualizeQuakes(6, 'earthquakes.txt', 7)
    return None


if __name__ == '__main__':
    main()


