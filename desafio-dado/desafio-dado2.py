from random import randint

def formatar(texto, center=False):
    print('-' * 40)
    if (center == True):
        print(texto.center(40))
    else:
        print(texto)
    print('-' * 40)


def jogarDado():
    numero = randint(1, 6)
    return print(f'\nO resultado da jogada foi: {numero}')


def checarResposta(resposta):
    if (resposta not in 'SN'):
        r = input('> Digite novamente: ').upper().split()[0]
        resposta = checarResposta(r)
    elif (resposta == 'N'):
        formatar('Obrigada por participar! :)', True)
    return resposta


def jogarPartida(jogou):
    if (jogou == 0):
        resp = input('> Deseja jogar o dado? [S/N] ').upper().split()[0]
        resp = checarResposta(resp)
        if (resp == 'S'):
            jogarDado()
            jogou = 1
            jogarPartida(jogou)

    elif (jogou == 1):
        resp = input('> Deseja jogar novamente? [S/N] ').upper().split()[0]
        resp = checarResposta(resp)
        if (resp == 'S'):
            jogarDado()
            jogarPartida(jogou)


formatar('DESAFIO DO DADO', True)
jogou = 0
jogarPartida(jogou)