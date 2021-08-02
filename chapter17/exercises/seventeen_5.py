import operator
class Point(object): 
    def __init__(self,x = 0,y =0): 
        self.x = x
        self.y = y
      

    def __str__(self): 
        return '(%d,%d)' % (self.x,self.y)

    def __add__(self,other): 
        if isinstance(other,Point): 
            return self.add_point(other)
        else: 
            return self.increment(other) 
   
    def add_point(self,other):
        point = Point() 
        point.x = self.x + other.y
        point.y = self.y + other.y 
        return point 

 
    def increment(self,other): 
        if isinstance(other,tuple): 
            self.x += other[0]
            self.y += other[1]
            return self
        else: 
            print "Input is not tuple"
            return self
    def __radd__(self,other): 
            return self.__add__(other)
    
    print "Example of polymerization"
    t1 = (7,43)
    t2 = (7,45)
    t3 = (7,37)
    total = sum([t1,t2,t3])
print total

start = Point(9,45)
end = Point(1,35)

print start+end
print start+(1,2)


