def main():
    inicio = 1
    alvo = int(input('Número: '))

    valor = inicio + 1


    while valor <= alvo:
        inicio = inicio + valor


        valor = valor + 1
    print(inicio)


main()