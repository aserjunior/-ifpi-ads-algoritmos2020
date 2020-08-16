def main():
    alvo = int(input('Escolha um número: '))
    inicio = 1
    atual = inicio


    while atual < alvo:
        if atual % 2 == 0:
            print(atual)


        atual = atual + 1


    print('Esses são os números pares que estão entre 1 e {}'. format(alvo))


main()