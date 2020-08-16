#Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão Geométrica que tem por valor inicial A0 e razão R.
def main():
    valor_inicial = int(input('Valor inicial: '))
    limite = int(input('Limite: '))
    razao = int(input('Razão: '))


    inicio = valor_inicial


    while valor_inicial * razao < limite:
        valor_inicial = valor_inicial * razao


        print(valor_inicial)


    print('Esses são os valores menores que o limite {} gerados pela PG de razão {} e valor inicial {}'.format(limite, razao, inicio))


main()