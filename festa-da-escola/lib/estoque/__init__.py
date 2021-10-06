from lib import style as s

options = ['Comprar fichas', 'Gastar fichas', 'Ver o Estoque']

def apresentarMenu():
    s.formatarTexto('MENU', type='menu_title')

    for i, item in enumerate(options):
        print(f'[{i + 1}] : {item}')

    print('-' * 50)

    op = input('> Escolha a opção desejada: ')
    return op