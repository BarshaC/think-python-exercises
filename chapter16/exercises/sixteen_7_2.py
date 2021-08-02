import datetime
from datetime import datetime, date, time

today = datetime.today()

m= int(raw_input("Month you were born: "))
d = int(raw_input("Day you were born:"))
my_birthday = datetime(today.year,m,d,00,00,0000)
if my_birthday < today: 
    my_birthday = my_birthday.replace(year = today.year+1)

time_to_birthday = abs(my_birthday-today)
print time_to_birthday





