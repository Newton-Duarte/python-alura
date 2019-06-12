import random


def jogar():
    print('*********************************')
    print('*Bem vindo ao jogo da Advinhação*')
    print('*********************************')

    tentativas = 0
    numero_secreto = random.randrange(1, 11)
    pontos = 1000

    print('Qual nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Digite o nível de dificuldade '))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, tentativas))
        chute = int(input('Qual número sorteado? ').strip())
        if (chute == numero_secreto):
            print('Você acertou! O número sorteado foi {}'.format(numero_secreto))
            break
        else:
            if (chute > numero_secreto):
                print('Errou, o seu chute foi maior que o número sorteado.')
            else:
                print('Errou, o seu chute foi menor que o número sorteado.')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print('Fim de jogo. Você fez {} pontos.'.format(pontos))

if (__name__ == '__main__'):
    jogar()