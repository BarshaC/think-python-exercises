def is_abecedarian(word):
    previous = word[0]
    if c in word:
        if c< previous: 
            print c 
            return False
        previous=c
    return True

