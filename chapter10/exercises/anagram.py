def anagram(lst1,lst2):
    res1=[]
    res2=[]
    for s in lst1:
        res1.append(s.upper())
    for r in lst2:
        res2.append(r.upper())
    res2.sort()
    res1.sort()
    if res1 == res2:
        print "The word you just entered are anagram,that is they have same letters arranged differently"
    else:
        print "No,they are not anagram"
anagram(str(raw_input("enter a word ")),str(raw_input("enter another word ")))

