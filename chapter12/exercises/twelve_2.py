import random
def sort_by_length(*words):
    t = []
    for word in words:
        t.append((len(word),word))
    t.sort()
    t.sort(reverse= True) #Here reverse=True makes list in descending order (from big to small) 
    res=[]
    for length,word in t:
        res.append(word)
    #return res
    print res
sort_by_length('barsa','ok','nice')
 
mylist = [2,3,1,'loren','pizza']
print random.choice(mylist)

