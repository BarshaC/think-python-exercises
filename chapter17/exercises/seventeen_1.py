class Time(object): 
    def __init__(self,hour = 0,minute = 0,second= 0): 
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self): 
        return '%.2d:%.2d:%.2d' % (self.hour,self.minute,self.second)

    def time_to_int(self):
        minutes = self.hour *60 +self.minute
        seconds = minutes*60 + self.second
        return seconds  

    def increment(start,seconds): 
        seconds += start.time_to_int() 
        return int_to_time(seconds)


def int_to_time(seconds): 
    time =Time() 
    minutes,time.second = divmod(seconds,60)
    time.hour, time.minute = divmod(minutes,60)
    return time

time = Time(9,45,0) 
print time

end = time.increment(1337)
print end 


