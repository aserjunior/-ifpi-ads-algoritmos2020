def main() :
    palavra = input('Palavra: ')    
    right_justify(palavra)

def right_justify(s) :
    tam_palavra = len(s)
    qtd_espacos = 70 - tam_palavra
    espacos = qtd_espacos * ' '
    resultado = espacos + s
    print(resultado)


main()