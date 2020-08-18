def main():
    n = int(input('Escolha um número: '))
    numero = n
    inicio = 1
    raiz = 0


    while inicio < numero:
        valor = inicio ** 0.5
        if valor % 1 == 0:
            raiz = valor


        inicio = inicio + 1


        quadrado = raiz ** 2


    print('>>> O quadrado mais próximo de {} é {} de raiz {}'.format(n, quadrado, raiz))


main()
