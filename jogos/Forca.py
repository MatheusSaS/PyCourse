def jogar():
    print("(*******************************")
    print("Bem vindo ao jogo de Forca!!")
    print("(*******************************")

    palavra_secreta = 'arroz'
    letras_acertadas =["_","_","_","_","_"]

    enforcou = False
    acertou = False
    print("{}".format(letras_acertadas))
    while(not enforcou and not acertou):
        chute = input("Qual Letra?")
        chute = chute.strip() #tira os espações em branco
        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print("{}".format(letras_acertadas))

if (__name__ == "__main__"):  # quando é rodado diretamente, seta como __main__
    jogar()
