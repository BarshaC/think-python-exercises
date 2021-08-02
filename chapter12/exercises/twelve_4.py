fin = open('words.txt','r')
l= dict()
for x in range(113810):
    word = fin.readline()
    word = word.strip() 
    t = tuple(word) 
    alis = sorted(t)  
    new_t= tuple(alis)
    l[new_t]  = word 
