import string
def right_justify(s):
    gap = string.whitespace()
    for k in range(0,70):
        gap = " " + s
        print(gap) 
    return str(s) + gap 
k = right_justify('monty')
print (k)

