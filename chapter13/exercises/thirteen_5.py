d = dict()
def histogram(s): 
    for c in s:  
        d[c] = 1 + d.get(c,0) 
    return d 
def choose_from_hist(d):
    h = histogram(s)
    total = 0 
    for k in d:
        total = total + d[k]  
    g = dict()
    for k in d:
        g[k] = float(d[k])/total
    return g
s ='bayernnunichvsparis' 
prob_d = choose_from_hist(d) 
print prob_d

        

