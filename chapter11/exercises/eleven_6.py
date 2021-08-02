known = {0:0,1:1}
def fibonacci(n):
    if n in known:
        print known[n]
        return known[n]
    res= fibonacci(n-1)+fibonacci(n-2)
    known[n] = res
    return res
fibonacci(15)
