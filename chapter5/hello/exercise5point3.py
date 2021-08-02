def check_fermat(a,b,c,n):
    if n<=2:
        g = int(c)**2
        h = (int(a)**2) + (int(b)**2)
        check_fermat(a,b,c, n+1)
    elif n>=2:
        g= int(c)**2
        h= (int(a)**2)+(int(b)**2)        
        if g==h:
            print "Holy smokes, Fermat was wrong"
        else:
            print "It does not work"
check_fermat(-2,-3,-5,0)

