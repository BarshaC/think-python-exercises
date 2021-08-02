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
def grow_rectangle(rect,dwidth,dheight): 
    rect.width += dwidth 
    rect.height += dheight
grow_rectangle(box,50,100)

def move_rectangle(move,dx,dy): 
    move.corner.x += dx
    move.corner.y += dy 
move_rectangle(box,12,16) 

center = find_center(box)
print 'After changing the position of the coordinate' 
print_point(center)

