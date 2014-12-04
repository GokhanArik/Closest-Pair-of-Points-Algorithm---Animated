import math
import random
import sys

def brute_force(X, n):

    min_d = distance(X[0], X[1])

    for i,(x,y) in enumerate(X):
        for j in range(i+1, n):
            if distance(X[i], X[j]) < min_d:
                min_d = distance(X[i], X[j])  

    return min_d

def distance(a,b):
    return math.sqrt( math.pow( (a[0]-b[0]), 2) + math.pow((a[1]-b[1]), 2) )

def gen_points(r):
    a=[]
    for i in range(1,r):
        a.append( (random.randint(1,1000), random.randint(1,1000)) )
    return a

############ Start Program ###############
points = [(2,3), (10, 1), (3, 25), (23,15),
         (18,3), (8,9), (12,30), (25,30),
         (9,2), (13,10), (3,4), (5,6),
         (22,32), (5,32), (23,9), (19,25),
         (14,1), (11,25), (26,26), (12,9),
         (18,9), (27,13), (32,13)]

if sys.argv[1] is not None:
    points = gen_points( int(sys.argv[1]) )

print points
print "\n\nMinimum distance between two points is %s" % brute_force(points, len(points))
