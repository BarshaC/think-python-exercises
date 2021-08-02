def in_love(name1,word, name2):
    letter = 'a'
    count = 0
    if letter in name1:
        if letter in word:
            if letter in name2:
                count = count +2 
            else:
                count = count +1
    print count
in_love(str("barsha"), str('loves'), str('food'))

