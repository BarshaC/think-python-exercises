fout = open('output.txt','w') 
line1 = "This is the moment you have to remember. \n"
fout.write(line1) 
line2 = "What moment you are taking about? \n"
fout.write(line2) 
d = 365 
line3= 'There are  %d, days in a year.You can remeber all of them.'  % d 
fout.close()
import os 
cwd = os.getcwd()
pw = os.path.abspath('output.txt')  
print cwd 
print pw

import anydbm 
db = anydbm.open('captions.db','c') 
db['cleese.png'] = 'Photo of John Cleese'
print db['cleese.png'] 
for key in db: 
    print key
db.close()

