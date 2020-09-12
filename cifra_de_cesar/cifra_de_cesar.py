def rotate_word():
    n = input('Escolha o texto:\n')
    valor = int(input('Escolha o número de rotações:\n'))
    texto_final = ''


    for letra in n:
        if ' ' in letra:
            nova_letra = ' '
            texto_final = texto_final + nova_letra
        else:
            rotar_letra = ord(letra) + valor
            nova_letra = chr(rotar_letra)
            texto_final = texto_final + nova_letra


    print('O codigo criptografado é: \n>>>{}'.format(texto_final))


rotate_word()