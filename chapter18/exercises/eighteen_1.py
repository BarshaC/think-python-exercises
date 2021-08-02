class Time(object): 
    #Time comparison

    def __init__(self,hours = 0,minutes = 0,seconds = 0):
        self.hours= hours
        self.minutes = minutes
        self.seconds = seconds
    time_hours = []
    time_minutes = []
    time_seconds = []
    for k in range(0,25): 
        time_hours.append(k)
    for l in range(0,61): 
        time_minutes.append(l)
        time_seconds.append(l)

    def __str__(self): 
        return '%.2d:%.2d:%.2d' % (Time.time_hours[self.hours],Time.time_minutes[self.minutes],Time.time_seconds[self.seconds]) 

    def __cmp__(self,other): 
        t1 = self.hours,self.minutes,self.seconds
        t2 = other.hours,other.minutes,other.seconds
        return cmp(t1,t2)

start = Time(1,20,17)
end = Time(2,18,10)
print cmp(start,end)

