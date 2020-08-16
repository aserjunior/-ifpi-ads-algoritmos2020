def main():   
    inicio = 1
    alvo = int(input('Escolha um número: '))
    limite = alvo - 1


    while inicio < limite:
        inicio = inicio + 1
        print(inicio)

        
    print('Esses são os números que estão entre 1 e {}'.format(alvo))


main()
