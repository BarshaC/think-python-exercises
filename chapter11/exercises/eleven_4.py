def histogram(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c,0)
    return d
g = histogram('parrot')
def reverse_lookup(d,v):
    list = []
    for k in d:
        if d[k] == v:
            list.append(k)
    else:
        print "no such keys exit"
    print list
    return k
    raise ValueError 
h= histogram('parrot')
k= reverse_lookup(h,3)




