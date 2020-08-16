def main():
    numero = int(input('Escolha um número: '))
    valor = numero - 1

    while valor - 1 > 0:
        numero = numero * valor
        valor = valor - 1
    print(numero)


main()