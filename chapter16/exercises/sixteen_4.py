class Time(object): 
    '''Time is an object 
       attributes : Hour, minute and second'''
start = Time() 
start.hour = 9
start.minute = 45 
start.second = 13

import copy

def increment(time,seconds): 
    print 'Original time is : %.2d:%.2d:%.2d' %(start.hour,start.minute,start.second)

    Newtime = copy.copy(start)
    Newtime.second += seconds
    
    if Newtime.second >= 60: 
        Newtime.second = (Newtime.second)%60 
        Newtime.minute +=(Newtime.second)//60
    if Newtime.minute>= 60: 
        Newtime.minute = Newtime.minute%60 
        Newtime.hour += Newtime.minute//60  
    if Newtime.hour> 12:
        Newtime.hour -= 12
    print 'New time is : %.2d:%.2d:%.2d' %(Newtime.hour,Newtime.minute,Newtime.second)
increment(start,560)
