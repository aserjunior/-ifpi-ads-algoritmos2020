def main():
    valor_inicial = int(input('Número incial: '))
    limite = int(input('Limite: '))
    razao = int(input('Razão: '))


    inicio = valor_inicial


    while valor_inicial < limite:
        if valor_inicial % razao == 0:
            print(valor_inicial)


        valor_inicial = valor_inicial + 1


    print('Esses são os valores gerados pela PA de razão {} menores que o limite {} e de valor inicial {}'.format(razao, limite, inicio))


main()
