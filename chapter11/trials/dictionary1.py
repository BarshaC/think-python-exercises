def histogram(s):
    d = dict()
    for j in s:
        d[j] = 1+ d.get(j,0)
    print d
histogram('parrot')
def print_hist(h):
    for c in h:
        print c, h[c]
print_hist('parr')
 
