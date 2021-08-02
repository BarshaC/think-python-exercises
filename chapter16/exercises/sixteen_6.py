class Time(object): 
    ''' Time is an object 
      attributes: hour, minutes and second'''
start = Time()
start.hour = 12
start.minute = 42
start.second = 39

finish = Time()
finish.hour = 13
finish.minute = 15
finish.second = 17

import copy

def mul_time(t,n): 
    new_Time = copy.copy(t)
    time = new_Time.hour *60*60 + new_Time.minute *60 + new_Time.second
    new_Time.product = time*n 
    return new_Time.product 

def average(time,n):
    f = copy.copy(finish)
    print "The finishing time: (%.2d:%.2d:%.2d)" %(f.hour,f.minute,f.second) 
    print 'distance: %g' %(n)
    t1= mul_time(start,4) 
    t2= mul_time(finish,4)
    print "Average speed in seconds per mile: ", (t2-t1)/float(n**2)
average(finish,4)
