def do_twice(f,g):
    f(g)
    f(g)
def print_twice(g):
    print g
    print g
def do_four (f,g):
    do_twice(f,g)
    do_twice(f,g)
do_four(print_twice,'spam')
print ''

