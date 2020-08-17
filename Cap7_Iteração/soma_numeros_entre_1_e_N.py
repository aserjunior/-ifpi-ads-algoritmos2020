def main():
    inicio = 2
    alvo = int(input('Número: '))


    atual = inicio + 1


    while atual < alvo:
        inicio = inicio + atual


        atual = atual + 1


    print('A soma dos números entre 1 e {} é igual a {}'.format(alvo, inicio))


main()