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
print 'Total number of words ussed in the book:', total_words(hist) 
print 'Number of different words in the book:', different_words(hist) 

def most_common(hist): 
    t = []
    for key, value in hist.items(): 
        t.append((value,key))
    t.sort(reverse=True)
    return t
 
t = most_common(hist) 

for freq, word in t[0:20]: 
    print word, '\t', freq

