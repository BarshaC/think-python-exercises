def histogram(s): 
    d = dict() 
    for c in s: 
        if c not in d: 
            d[c] = 1
        else: 
            d[c] +=1
    return d

t = ['spam','egg','spam','spam','bacon','spam']
h= histogram(t)
print h
