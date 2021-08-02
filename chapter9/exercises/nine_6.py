f = list()
def is_abecedarian(word):
    for letter in word.lower(): 
        f.append(letter) 
        f.sort()
    print f
is_abecedarian("Hariyana")

