def duplicar(f) :
    f()
    f()

def quadruplicar(f) :
    duplicar(f)
    duplicar(f)

def linha_1() :
    print('+ - - - -', end=' ')

def barra() :
    print('|        ', end=' ')  

def linhas_1() :
    duplicar(linha_1)
    print('+')

def barras() :
    duplicar(barra)
    print('|')

def grade() :
    linhas_1()
    quadruplicar(barras)

def fazer_grade() :
    duplicar(grade) 
    linhas_1()

fazer_grade()   