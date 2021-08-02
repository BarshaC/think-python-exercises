def rotate(s,n):
    lookover='abcdefghijklmnopqrstuvwxyz'
    ans = ''
    for letter in s:
        index = lookover.index(letter)
        if n>0:
            new_index = (index+n)%26
        else:
            n = n%26
            new_index = (index +n)%26
        ans = ans + lookover[new_index]
    print ans
rotate('cheer',7)

