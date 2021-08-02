def print_n(s,n):
    if n>=0:
        print s
        print_n(s,n-1)
print_n('Hello',2)
