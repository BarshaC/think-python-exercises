f = open('words.txt') 
h = []
list_anagram =[] 
d = dict()
for k in range(24500): 
    fin = f.readline()
    words = fin.strip()  
    h.append(words) 
five = []
for l in range(24500): 
    t = h[l]
    char = len(sorted(tuple(t)))
    git = tuple(t) 
    if char ==5: 
       five.append(h[l])
count = 1
anagram = []
while count<len(five):
    for f in range(2,len(five)):
        word = five[count]
        word_1 = list(sorted(tuple(five[count])))
        word_2 = list(sorted(tuple(five[f])))
    if word_1 == word_2: 
       anagram.append(word)
    count = count + 1
print anagram
