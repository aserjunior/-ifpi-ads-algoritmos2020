def main():
    inicio = 1
    alvo = int(input('Número: '))

    valor = inicio + 1


    while valor <= alvo - 1:
        inicio = inicio + valor


        valor = valor + 1


    print('A soma dos inteiros entre 1 e {} é {}'.format(alvo, inicio - 1))


main()