import math
def hypotenuse(b,h):
    value = math.sqrt(b**2+h**2)
    print value
    return value 
hypotenuse(float(raw_input("HEIGHT OF TRIANGLE :")),float(raw_input("BASE :")))

