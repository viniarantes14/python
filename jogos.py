import forca
import adivinhacao


def escolhe_jogo():

    imprime_mensagem_inicial()

    define_jogo()


def imprime_mensagem_inicial():
    print("Bem vindo ao menu, selecione o jogo desejado")

    print("\n\n(1) Forca (2) Adivinhação")


def define_jogo():
    jogo = int(input("\nQual jogo?\n "))

    if (jogo == 1):
        print("\nJogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("\nJogando adivinhação")
        adivinhacao.jogar()


if(__name__ == "__main__"):
    escolhe_jogo()