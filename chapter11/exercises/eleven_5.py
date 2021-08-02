def histogram(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c,0)
    return d
def invert_dict(d):
    inverse = dict()
    for key in d:
        print d[key]
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
hist= histogram('parrot')
print hist 
inverse = invert_dict(hist)
print inverse
