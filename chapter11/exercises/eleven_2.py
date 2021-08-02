d = dict()
def histogram(s):
    for c in s:
        d[c] = 1 + d.get(c,0)
    print d
histogram('parrot')

