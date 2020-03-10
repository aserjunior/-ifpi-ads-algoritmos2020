def do_twice(f,g) :
    f(g)
    f(g)

def print_spam(valor) :
    print(valor)

def do_four(f,g) :
    f(g)
    f(g)

do_twice(print_spam, 'spam')

do_four(print_spam, 'spam')    