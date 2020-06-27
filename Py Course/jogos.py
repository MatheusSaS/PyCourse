import Forca
import adivinhacao

def escolha():
    print("(*******************************")
    print("******* Escolha seu jogo *******")
    print("(*******************************")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual Jogo: "))

    if(jogo == 1):
        print("Jogo da Forca")
        Forca.jogar()
    else:
        print("Jogo Adivinhação")
        adivinhacao.jogar()
if(__name__ == "__main__"):
    escolha()
