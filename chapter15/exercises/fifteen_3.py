class Point(object): 
    '''Represents a point'''

def print_point(p): 
    print'(%g,%g)' % (p.x, p.y) 

class Rectangle(object): 
    '''Represents a rectangle.
       attributes: width, height, corner.
    '''
box = Rectangle() 
box.width = 100.0
box.height = 200.0

box.corner = Point() 
box.corner.x = 0.0
box.corner.y = 0.0 

def find_center(rect): 
    p = Point() 
    p.x = rect.corner.x + rect.width/2 
    p.y = rect.corner.y + rect.height/2
    return p
import copy 
box2 = copy.copy(box) 
box.corner2 = copy.copy(box.corner)

'''Class allows the copying the objects. Here, the new rectangle is formed with the same attributes. But they are not same '''
center = find_center(box2)
print 'Calling a new rectangle' 
print_point(center)

