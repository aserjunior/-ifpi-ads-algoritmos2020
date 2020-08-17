def main():
    limite_inferior = int(input('Limite Inferior: '))
    limite_superior = int(input('Limite Superior: '))


    pares = limite_inferior + 1


    while pares < limite_superior:
        if pares % 2 == 0:
            print(pares)


        pares = pares + 1


    print('>>> Esses são os pares presentes entre {} e {}'. format(limite_inferior, limite_superior))


main()