from lib import style as s

def apresentar_menu(list):
    s.formatarTexto('MENU', type='menu_title')

    for i, item in enumerate(list):
        print(f'[{i + 1}] : {item}')


def comprar_fichas():
    print('Olá, eu sou o Caixa Geral!')
    quantidade = int(input('> Quantas fichas deseja comprar?'))
    print(quantidade)

#def gastar_fichas():
#def ver_estoque():
