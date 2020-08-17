def main():
    tabuada = int(input('Escolha a tabuada de 1 a 10: '))


    numero_fixo = tabuada
    valor_multiplicado = 1


    while  valor_multiplicado <= 10:
        resultado = valor_multiplicado * numero_fixo


        print(resultado)


        valor_multiplicado = valor_multiplicado + 1


    print('>>> Acima é apresentado a tabuada de {}'.format(tabuada))


main()
