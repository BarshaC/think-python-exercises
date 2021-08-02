f = open("words.txt","r")
lst = dict()
for k in range(113809):
    word = f.readline()
    word = word.strip()
    lst[word] = 1
print lst


