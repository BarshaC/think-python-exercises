def has_no_e(word):
    word.lower()
    for letter in word:
        if letter == 'e' :
            print "YEs the word has e"     
            return            
    print "There is no e " + 'in the word : '+ word
has_no_e(raw_input("Enter a word: "))

             
            

