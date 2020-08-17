def main():
    numero = int(input('Escolha um número: '))
    inicio = numero

    valor = numero - 1


    while valor > 0:
        numero = numero * valor
        valor = valor - 1


    print('>>> O fatorial de {} é {}'.format(inicio, numero))


main()
