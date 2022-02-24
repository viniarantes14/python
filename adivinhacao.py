import random


def jogar():

    mensagem_abertura()

    total_de_rodadas = seleciona_dificuldade()

    # variaveis
    vidas = total_de_rodadas  # vidas é usada como condição para imprimir a mensagem de derrota
    rodada = 1
    pontos = 1000
    numero_secreto = sorteio()

    # algoritmo
    for rodada in range(0, total_de_rodadas):

        informa_rodada(rodada, total_de_rodadas)

        chute = recebe_chute()
        pontos = calcula_pontos(numero_secreto, chute, pontos)

        validacao_intervalo = valida_intervalo(chute)

        validacao = True
        validacao = logica(numero_secreto, chute, vidas, pontos)

        if(validacao == False):
            break

        verifica_vidas(vidas, numero_secreto)


def mensagem_abertura():
    print("Bem vindo ao jogo de adivinhação! ")
    print("\n\n(1) Fácil (2) Médio (3) Difícil\n")


def seleciona_dificuldade():
    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_rodadas = 20
        return total_de_rodadas
    elif (nivel == 2):
        total_de_rodadas = 10
        return total_de_rodadas
    else:
        total_de_rodadas = 5
        return total_de_rodadas


def sorteio():
    numero_sorteado = random.randrange(1, 101)
    return numero_sorteado


def informa_rodada(rodada, total_de_rodadas):
    print("Rodada {} de {}".format(rodada + 1, total_de_rodadas))


def recebe_chute():
    chute = int(input("\nDigite um número entre 1 e 100:\n"))
    return chute


def calcula_pontos(numero_secreto, chute, pontos):
    pontos_perdidos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perdidos
    return pontos


def valida_intervalo(chute):
    if (chute < 1 or chute > 100):
        print("\nDigite um valor entre 1 e 100!\n")
        return False
    else:
        return True


def logica(numero_secreto, chute, vidas, pontos):
    acertou = numero_secreto == chute
    maior = numero_secreto > chute
    menor = numero_secreto < chute

    if (acertou):
        print("\nParabéns, você acertou! e fez {} pontos".format(pontos))
        vidas = -1
        return False

    else:
        if (maior):
            print("\nO número secreto é maior")

        elif (menor):
            print("\nO número secreto é menor")

    vidas -= 1


def verifica_vidas(vidas, numero_secreto):
    if (vidas == 0):
        print("\nVocê perdeu, o número secreto era {} e fez 0 pontos,por favor reinicie o jogo!".format(numero_secreto))


if(__name__ == "__main__"):
    jogar()