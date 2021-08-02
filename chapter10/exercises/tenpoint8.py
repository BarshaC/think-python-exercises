#Asks 23 people about their birthday and looks for birthday twins
def ranint():
    lst = []
    n =1
    for x in range (0,23):
        g = raw_input ("Enter your birthdate: ")   
        lst.append(g.upper())
    for r in lst:
        for j in lst[n:]:
            n +=n
            if r == j:
                print "Your class has birthday twin for sure"
                print "Who are the lucky ones who have birthday on" +str(r)
            else:
                print "You all have unique birth dates"
ranint()    

        
