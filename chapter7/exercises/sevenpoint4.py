import math
def eval_loop():
    n=6 
    while n>=0:
        n= n-1
        eval = float(raw_input("Enter a number: "))
        print "The square root of the number your enter is"+ str(math.sqrt(eval))
eval_loop()
