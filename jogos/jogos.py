import forca
import advinhacao

def escolhe():
    print("****************************")
    print("{:*^28}".format("Escolha um jogo"))
    print("****************************")

    print("(1) Forca (2)Advinhação")
    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()

    elif(jogo==2):
        print("Jogando Advinhação")
        advinhacao.jogar()

if(__name__ == "__main__"):
    escolhe()
