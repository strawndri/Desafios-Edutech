from random import randint


def formatar(texto, center=False):
    print('-' * 40)
    if (center == True):
        print(texto.center(40))
    else:
        print(texto)
    print('-' * 40)


def jogaDado():
    numero = randint(1, 6)
    return numero


formatar('DESAFIO DO DADO', True)


def perguntar():
    resposta = input('> Deseja Jogar o Dado? [S/N] ').upper().split()[0]

    if (resposta not in 'SN'):
        formatar('[ERRO] Digite uma resposta válida. ', True)
        perguntar()
    elif (resposta == 'S'):
        formatar(f'Resultado da jogada: {jogaDado()}')
        perguntarNovamente()
    else:
        print('Obrigada por participar! :)')


def perguntarNovamente():
    resposta = input('> Deseja Jogar Novamente? [S/N] ').upper().split()[0]

    if (resposta not in 'SN'):
        formatar('[ERRO] Digite uma resposta válida. ', True)
        perguntarNovamente()
    elif (resposta == 'S'):
        formatar(f'Resultado da jogada: {jogaDado()}')
        perguntarNovamente()
    else:
        formatar('Obrigada por participar! :)', True)


perguntar()