def main():
    contador = 0
    inicio = 1
    alvo = int(input('Escolha um número: '))
    limite = alvo - 1


    while inicio < limite:
        inicio = inicio + 1
        print(inicio)

        contador = contador + 1


    print('Esses são os números que estão entre 1 e {}'.format(alvo))


main()