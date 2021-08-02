class Time(object): 
    '''Represents time as an object 
    with attribute: Hour, minute, seconds'''
time = Time() 

def print_time(t): 
    print '%.2d:%.2d:%.2d' %(t.hour,t.minute,t.second)

def increment(t1,t2): 
    sum = Time() 
    sum.second = (t1.second + t2.second)%60
    sum.minute = (t1.minute + t2.minute)%60 + ((t1.second+t2.second)//60) 
    sum.hour = (t1.hour + t2.hour) + ((t1.minute+t2.minute)//60)
    return sum 
start = Time() 
start.hour = 9 
start.minute = 45
start.second = 45 

duration = Time() 
duration.hour = 1
duration.minute = 35
duration.second = 48 

done = increment(start,duration) 
print_time(done) 


