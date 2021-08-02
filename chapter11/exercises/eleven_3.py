
def histogram(s):
    d = dict()
    for c in s:
         d[c] = 1 + d.get(c,0)
    return d
g= histogram ('eleven')
def print_hist(h):
    list_keys = h.keys()
    #print list_keys
    list_keys.sort()
    print list_keys
    for j in list_keys:
        print j, h[j]
h= histogram('hipp')
print_hist(g)
print_hist(h)

