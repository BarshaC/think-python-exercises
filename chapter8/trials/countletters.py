def coun_t(string,letter):
    count = 0
    for lett_er in string:
        if lett_er == letter:
            count = count+1 
    print "There are " +str(count), letter, " in the string",string
coun_t(str(raw_input('Enter any word :')),str(raw_input("Letter that you want to count in the word: ")))


