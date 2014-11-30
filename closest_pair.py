import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.pyplot import pause

plt.ion()
colors = []
p = None 

def plot_points(points):
    global colors
    global p

    X = []
    Y = []
    axis = []
    
    # Find X and Y values of points 
    for (x,y) in points:
        X.append(x)
        Y.append(y)

    # Set up X and Y axises
    axis.append(0)
    axis.append(max(X)+1)
    axis.append(0)
    axis.append(max(Y)+1)
    
    # Set up node area
    area = [100]*len(points)

    # Set up colors
    colors = [0.1]*len(points)

    p = plt.scatter(X, Y, s=area, c=colors)
    plt.axis(axis)
    plt.xticks(np.arange(0, max(X)+1, 1.0))
    plt.yticks(np.arange(0, max(Y)+1, 1.0))
    plt.grid(True)
    plt.show()

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

    # Draw vertical line in the middle
    draw_line(X[mid][0])
    pause(4)

    print "Middle:", X[mid]
    
    for p in Y:
        if p in X[:mid]:
            Y_Left.append(p)
        else:
            Y_Right.append(p) 
    
    print "Y_RIGHT: %s" % Y_Right
    print "Y_LEFT : %s" % Y_Left

    dis_left  = closest_pair(X[:mid], Y_Left, mid)
    dis_right = closest_pair(X[mid:], Y_Right, n-mid)

    min_dis = min(dis_left, dis_right)
    
    print "min_dis: %s" % min_dis
     
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
    global p
    min_d = distance(X[0], X[1])
    points = p.get_offsets().tolist()

    for i,(x,y) in enumerate(X):
        for j in range(i+1, n):
            if distance(X[i], X[j]) < min_d:
                min_d = distance(X[i], X[j])  
                colors[points.index([X[j][0],X[j][1]])]=0.5
                colors[points.index([x,y])]=0.5
                plt.text(x+1, y+1, min_d, ha='left', rotation=15)
                draw_line_points(X[i], X[j])
            else:
                colors[points.index([X[0][0],X[0][1]])]=0.5
                colors[points.index([X[1][0],X[1][1]])]=0.5
                draw_line_points(X[0],X[1])
                plt.text(X[0][0]+1, X[0][1]+1, min_d, ha='left', rotation=15)
 
    pause(4)   
    
    A=[]
    B=[]
    area = [100]*len(points)

    for x,y in p.get_offsets():
        A.append(x)
        B.append(y)
    plt.scatter(A,B,s=area,c=colors)
                  
    return min_d

# Draws vertical line for x value
def draw_line(x):
    y_max = int(max(plt.yticks()[0]))

    line_y = range(0, y_max+1,1)
    line_x = [x]*len(line_y)
    line, = plt.plot(line_x,line_y,linewidth=2)

# Draw line between two points 
def draw_line_points(a,b):    
    x=[]
    x.append(a[0])
    x.append(b[0])

    y=[]
    y.append(a[1])
    y.append(b[1])

    line, = plt.plot(x,y,linewidth=1)

########## Start Program ########

# 1. Create a list of points
points = [(2,3), (12,30),(25,30), (9,2), (13,10), (3,4), (5,6), (18,9), (27,13), (32,13)]

# 2. Draw points on graph
plot_points(points)

# 3. Solve the problem 
print "Minimum distance between two points is %s" % closest(points, len(points))

