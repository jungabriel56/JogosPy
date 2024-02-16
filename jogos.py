import forca
import advinhacao

def escolha_jogo():
    print("*********************************")
    print("Escoha o seu jogo")
    print("*********************************")

    print("(1) Forca (2) Advinhacao")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando advinhacao")
        advinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()