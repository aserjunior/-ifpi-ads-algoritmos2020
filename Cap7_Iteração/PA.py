#Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão Aritmética que tem por valor inicial A0 e razão R.
def main():
    valor_inicial = int(input('Número inicial: '))
    limite = int(input('Limite: '))
    razao = int(input('Razão: '))


    inicio = valor_inicial


    while valor_inicial + razao < limite:
        valor_inicial = valor_inicial + razao
        print(valor_inicial)


    print('Esses são os valores gerados pela PA de razão {} menores que o limite {} e de valor inicial {}'.format(razao, limite, inicio))


main()