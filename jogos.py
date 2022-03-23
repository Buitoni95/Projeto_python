import adivinhacao_for
import forca

def escolhe_jogo():

    print("*****************")
    print("Escolha seu jogo.")
    print("*****************")


    print("(1) Adivinhação (2) Forca:")

    jogo = int(input("Qual jogo?"))

    while(jogo < 1 or jogo > 2):
        print("Código de jogo inválido") 
        jogo = int(input("(1) Adivinhação (2) Forca:"))


    if(jogo == 1):
        print("Jogando Adivinhação")
        adivinhacao_for.jogar()
    else:
        print("Jogando Forca")
        forca.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()