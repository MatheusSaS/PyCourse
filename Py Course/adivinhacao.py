import random

def jogar():
    print("(*******************************")
    print("Bem vindo ao jogo de adiviação!!")
    print("(*******************************")

    num_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print("Qual o gral de dificuldade?")
    print("(1) Facil (2) Medio (3) Dificil")

    nivel = int(input("Defina seu nivel: "))
    print("Voce iniciara com 1000 pontos, Boa Sorte!!")

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for n_tentativa in range(1,tentativas + 1):
        print("\nTentativa  {}  de  {} ".format(n_tentativa, tentativas))
        tentativa_str = input("Digite o seu numero.: ")
        num = int(tentativa_str)
        acertou = num_secreto == num
        maior = num < num_secreto
        menor = num > num_secreto
        if(num < 1 or num > 100):
            print("So é permitido numeros entre 1 e 100")
            continue #volta para o laço
        if (acertou):
            print("voce acertou!!")
            print("Pontos {}".format(pontos))
            break
        else:
            print("voce errou")
            pontosPerdidos = abs(num_secreto - int(tentativa_str))
            pontos = pontos - pontosPerdidos
            print("Pontos restantes: {}".format(pontos))
            if(maior):
                print("voce chutou um nomero abaixo do correto")
            elif(menor):
                print("voce chutou um numero acima do correto")

if(__name__ == "__main__"): #quando é rodado diretamente, seta como __main__
    jogar()