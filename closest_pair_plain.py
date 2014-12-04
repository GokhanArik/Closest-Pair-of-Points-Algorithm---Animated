# Gokhan Arik 
#
#
# Python implementation of Closeset Pair of Points Function 
# /usr/bin/time  python brute_force.py 100
# /usr/bin/time  python closest_pair_plain.py 100

import numpy as np
import math
import random
import sys

# Trigger function for closest_pair function
def closest(P, n):
                                                    
    X=list(P)
    Y=list(P)

    X.sort()
    Y = sort_y(Y)
    return closest_pair(X, Y, n)

# Recursive Closest Pair function
def closest_pair(X, Y, n):
   
    if n <= 3:
            return brute_force(X, n)
             
    mid = n/2 
    Y_Left  = []
    Y_Right = [] 

    
    for p in Y:
        if p in X[:mid]:
            Y_Left.append(p)
        else:
            Y_Right.append(p) 
    

    dis_left  = closest_pair(X[:mid], Y_Left, mid)
    dis_right = closest_pair(X[mid:], Y_Right, n-mid)

    min_dis = min(dis_left, dis_right)
    
     
    strip  = [] 

    for (x,y) in Y:
        if abs( x - X[mid][0] ) < min_dis:
            strip.append((x,y))
    return min(min_dis, strip_closest(strip, min_dis))

# Utility function to calculate min distance between points in strip  
def strip_closest(strip, d):
    min_d = d
    for i,(x,y) in enumerate(strip):
        for j in range(i+1, len(strip)):
            if (strip[j][1] - strip[i][1]) < min_d and distance(strip[i], strip[j]) < min_d:
                min_d = distance(strip[i], strip[j])
    return min_d                   

# Calculates the distance between two points     
def distance(a,b):
    return math.sqrt( math.pow( (a[0]-b[0]), 2) + math.pow((a[1]-b[1]), 2) ) 

# Sort points by x value
def sort_y(tuples):
  return sorted (tuples,key=lambda last : last[-1])

# Brute force method to calculate distance for n<=3
def brute_force(X, n):
    min_d = distance(X[0], X[1])

    for i,(x,y) in enumerate(X):
        for j in range(i+1, n):
            if distance(X[i], X[j]) < min_d:
                min_d = distance(X[i], X[j])  
    
    return min_d

# Random array of points generator
def gen_points(r):
    a=[]

    for i in range(1,r):
        a.append( (random.randint(1,1000), random.randint(1,1000)) )
    return a

########## Start Program ########

if sys.argv[1] is not None:
    points = gen_points( int(sys.argv[1]) )
    print points 

print "\n\nMinimum distance between two points is %s" % closest(points, len(points))

