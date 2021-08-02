def avoids(word,string):
    for letter in word:
        if letter == string:
            return True
        else:
            print "THe word contains the fornidden letter"

