class Time(object): 
    ''' Time is an object
         Attributes: Hour, minute, second'''
time = Time()
time.hour = 8
time.minute = 29
time.second = 53

def print_time(t): 
    print 'The time initially %.2d:%.2d:%.2d' %(t.hour,t.minute,t.second) 
print_time(time)

def increment(time,seconds): 
    minutes = time.hour*60 + time.minute
    seconds = time.second + minutes*60 
    time = Time()
    minutes, time.second = divmod(seconds,60)
    time.hour, time.minute = divmod(minutes,60)
    print'The time after %g seconds : %.2d:%.2d:%.2d' %(seconds,time.hour,time.minute,time.second)
increment(time,975)







