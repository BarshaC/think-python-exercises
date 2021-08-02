def histogram(s):
    d= dict()
    for c in s:
        d[c] = 1 + d.get(c,0)
    print d
histogram('hills')
