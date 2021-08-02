def compare(x,y):
    if x>y:
        return 1
    elif x==y:
        return 0
    else:
        return -1
compare(int(raw_input("Enter one number")),int(raw_input("Enter another number")))
