import string

def process_file(filename): 
    hist = dict() 
    f = open(filename) 
    for line in f: 
        process_line(line,hist) 
    return hist
def process_line(line,hist): 
    line = line.replace('-',' ') 
    
    for word in line.split(): 
        word = word.strip(string.punctuation + string.whitespace) 
        word = word.lower() 
        hist[word] = hist.get(word,0) + 1
hist = process_file('book.txt') 


def random_string():
    leest =[]
    for key in hist: 
        leest.append(key) 
    import random
    for k in range(1,10): 
        x = random.randint(0,len(leest))
        y = leest[x] 
        print y,
word = random_string() 
def bisection():
    target = random_string()
    count = 0 
    low = 0 
    high= len(leest) -1 
    found = False
    while found== False and count < len(leest): 
        mid = (high+low)//2
        num = leest[mid] 
        print num
        if num == target: 
           print "The number is"; num
           found = True
        elif target < num: 
           high = mid
        else: 
           low = mid
        count = count + 1
bisection()

