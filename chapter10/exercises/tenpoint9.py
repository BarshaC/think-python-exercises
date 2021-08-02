def has_duplicates():
    f = ['g','h','o','k','l','g']
    n= 1
    for j in f:
        for c in f[n:]:
            n =n+1 
            if j ==c:
                print "yo it has dublicates"
                del f[n-1]
                print f
                
has_duplicates()      
