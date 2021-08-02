f = open('wrds.txt','r') 
lst = dict()
n =0
for line in range(113809):
    word = f.readline()
    word = word.strip()
    lst[word] = 1
print lst

