def do_twice(f,g):
    f(g)
    f(g)
def print_twice(g):
    print g
    print g
do_twice(print_twice,'spam')
print''


