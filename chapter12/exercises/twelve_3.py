def most_frequent(word):
    decreasingly_order=[]
    letters = tuple(word)
    for letter in letters:
        decreasingly_order.append(letter)
    decreasingly_order.sort()
    print decreasingly_order
most_frequent('barsha')

