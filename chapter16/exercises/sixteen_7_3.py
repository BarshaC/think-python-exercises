import datetime
from datetime import datetime, date, time

today = date.today()

def input_birthdays(year,month,day):
    birthday = date(year,month,day)
    return birthday
x = input_birthdays(2000,06,11)
y = input_birthdays(2005,05,11)

if x.year<y.year: 
    diff = y.year -x.year
    dday = y.year + diff
    print req_day
else:
    diff = x.year-y.year
    req_day = y.year + diff 
    print req_day
