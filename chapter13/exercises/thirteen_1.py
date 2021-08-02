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
def total_words(hist): 
    return sum(hist.values())
def different_words(hist):
    return len(hist)
 
print 'total number of words:',total_words(hist)
print "NUmber of different words",different_words(hist) 


