def main():
    limite_inferior = int(input('Limite Inferior: '))
    limite_superior = int(input('Limite Superior: '))

    impares = limite_inferior + 1


    while impares < limite_superior:
        if impares % 2 != 0:
            print(impares)


        impares = impares + 1


    print('>>> Esses são os ímpares que estão entre {} e {}'.format(limite_inferior, limite_superior))


main()