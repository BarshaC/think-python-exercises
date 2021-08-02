import math
def distance(x1,y1,x2,y2):
    radius = math.sqrt(float((x2-x1))**2+float((y2-y1))**2)
    return radius
def area(radius):
    result= math.pi*radius*2.0
    return result
def circle_area(x1,y1,x2,y2):
    return area(distance(x1,y1,x2,y2)) 
circle_area(1,6,4,10)

