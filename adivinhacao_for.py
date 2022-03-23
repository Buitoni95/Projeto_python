import random


def jogar():
    print("***********************************")
    print("Bem vindo ao jogo de adivinhação.")
    print("***********************************")

    numero_secreto = random.randrange(1,101) 
    total_de_tentativas = 0
    pontos = 1000

    print("Escolha o nível de dificuldade")
    dificuldade = int(input("(1) Fácil (2) Médio (3) Difícil:"))


    while(dificuldade < 1 or dificuldade > 3):
        print("Nível de dificuldade inválido, digite novamente") 
        dificuldade = int(input("(1) Fácil (2) Médio (3) Difícil:"))
        
    if(dificuldade == 1):
        total_de_tentativas = 30
    elif(dificuldade == 2):
        total_de_tentativas = 20
    else:
        total_de_tentativas = 10

    for rodada in range (1, total_de_tentativas +1):
        print("Tentativa: {}  de {}".format(rodada, total_de_tentativas))
        #print(numero_secreto)
        chute = int(input("Digite o seu número: "))

        if (chute < 1 or chute > 100):
            print("você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        print("você digitou", chute)

        if (acertou):
            print("você acertou parabéns!")
            print("Você ganhou com {}".format(round(pontos)))
            break
        else:
            if(chute_maior):
                print("Você errou, seu chute foi maior que o número secreto")
            elif(chute_menor):
                print("Você errou, seu chute foi menor que o número secreto")
            ponto_perdidos = abs (chute - numero_secreto) / 3
            pontos = pontos - ponto_perdidos

    if(total_de_tentativas == 0):
        print("Não foi dessa vez. O número secreto era {}". format(numero_secreto))

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()