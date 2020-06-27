def jogar():
    print("(*******************************")
    print("Bem vindo ao jogo de Forca!!")
    print("(*******************************")

    palavra_secreta = 'arroz'
    enforcou = False
    acertou = False
    while(not enforcou and not acertou):
        chute = input("Qual Letra?")
        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                print("Acertou a letra {} na prosição {}".format(chute,index))
            index = index + 1



        print("")

if (__name__ == "__main__"):  # quando é rodado diretamente, seta como __main__
    jogar()
