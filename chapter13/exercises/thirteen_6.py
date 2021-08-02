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
        w = word.split('/') 
        hist[w] = hist.get(w,0) + 1
hist = process_file('book.txt')
words = process_file('words.txt') 

def subtract(d1,d2): 
    f1 = {''}
    f2 = {''}
    for key in d1: 
        f1.add(key) 
    for key in d2:
        f2.add(key) 
    print f1-f2  
        

diff = subtract(hist,words) 

