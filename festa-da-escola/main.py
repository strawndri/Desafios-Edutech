from lib import style as s
from lib import estoque as e

options = ['Comprar fichas', 'Gastar fichas', 'Ver o Estoque']


s.formatarTexto('Bem-Vinda(o) à Festa Escolar!', type='title')
e.apresentarMenu(options)

print('-' * 50)

while True:

    try:
        op = int(input('> Escolha a opção desejada: '))
    except ValueError:
        print('[ERRO] - A opção digitada é inválida.')
    else:
        if (op > 0 and op <= 3):
            print(f'Você escolheu: {options[op - 1]}')
            break
        else:
            print('[ERRO] - A opção digitada é inválida.')