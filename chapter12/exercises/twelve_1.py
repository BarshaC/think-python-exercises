def sumall(*args):
    l = len(args)
    total = 0
    for k in range(0,l):
        total = total + args[k] 
    print total
sumall(3,4,5,8,19)


