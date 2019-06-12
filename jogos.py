import advinhacao
import forca


def escolha_jogo():

    print('*********************************')
    print('*****Escolha o jogo desejado*****')
    print('*********************************')

    print('(1) Advinhação (2) Forca')

    jogo = int(input('Qual jogo?'))

    if (jogo == 1):
        print('Jogando Advinhação')
        advinhacao.jogar()
    else:
        print('Jogando Forca')
        forca.jogar()

if (__name__ == '__main__'):
    escolha_jogo()