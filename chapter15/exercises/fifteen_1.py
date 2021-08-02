class Point(object): 
    'This makes a point in 2-D'
blank = Point()  
blank.x1 = 3.0 
blank.y1 = 4.0 
blank.x2 = -5.0
blank.y2 = 12.0
def print_point(b):
    print '(%g,%g) and (%g,%g)' %(b.x1,b.y1,b.x2,b.y2) 
r= print_point(blank)

import math
def distance_between_points(p):
    distance= math.sqrt((p.x2-p.x1)**2 + (p.y2-p.y1)**2)
    print 'distance between two points above is: ',distance
distance_between_points(blank)

