import random

def jogar():


    print("****************************")
    print("Bem vindo ao jogo Advinhacao")
    print("****************************")


    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual nível você deseja escolher?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if(nivel==1):
        total_de_tentativas = 20
    elif(nivel== 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite um número entre 1 e 100: ")
        chute = int(chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        errou_maior = chute > numero_secreto
        errou_menor = chute < numero_secreto

        if(acertou):
            print("Voce acertou e fez {} ", format(pontos))
            break
        else:
            if(errou_maior):
                print("Voce errou, seu chute foi maior")
            elif(errou_menor):
                print("Voce errou, seu chute foi menor")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos


    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()
