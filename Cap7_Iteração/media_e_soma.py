def main():
    n = int(input('Escolha a quantidade de números para a sua lista: '))
    numeros = n
    inicio = 1
    soma = 0


    while inicio <= numeros:
        valor = int(input('Escolha um Número: '))
        soma = soma + valor


        inicio = inicio + 1


    media = soma / n


    print('A soma dos números escolhidos foi {} e a media dessa lista de {} números é {}'.format(soma, n, media))


main()