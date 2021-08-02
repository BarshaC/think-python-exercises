class Time(object): 
    '''Represemts the time of day.
    attributes: hour, minute, second'''
time = Time() 
time.hour = 11
time.minute = 59 
time.second = 30 

def print_time(ti): 
    print '%.2d:%.2d:%2d' %(t.hour,t.minute,t.second) 
print_time(time) 

