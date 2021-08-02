n= 10
l = dict()
f = open('words.txt','r') 
for k in range (113808):
    word = f.readline()
    word = word.strip()
    lookover= 'abcdefghijklmnopqrstuvwxyz'
    ans =''
    for letter in word:
        index = lookover.index(letter) 
        if n>0: 
            new_index = (index+n)%26
        else: 
            n = n%26
            new_index = (index+n)%26 
        ans = ans +lookover[new_index]
    l[word] = ans 
    if ans in l: 
        print word + "=====" + ans 

 


   

