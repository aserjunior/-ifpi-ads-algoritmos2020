def main():
    n = int(input('Escolha a quantidade de números para a sua lista: '))
    numeros = n
    inicio = 1
    maior = 0

    while inicio <= numeros:
        valor = int(input('Escolha um número: '))
        if valor > maior:
            maior = valor


        inicio = inicio + 1


    print('>>> O maior valor dessa lista é {}'.format(maior))


main()