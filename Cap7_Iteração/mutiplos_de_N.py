def main():
    n = int(input('Número: '))
    limite_inferior = int(input('Limite Inferior: '))
    limite_superior = int(input('Limite Superior: '))


    multiplos = limite_inferior + 1


    while multiplos < limite_superior:
        if multiplos % n == 0:
            print(multiplos)


        multiplos = multiplos + 1


    print('>>> Esses são os múltiplos de {} que estão entre {} e {}'.format(n, limite_inferior, limite_superior))


main()
