from lib import style

def apresentar_menu(list):

    style.formatar_texto('Menu Principal', tipo='menu')
    for i, item in enumerate(list):
        print(f"[{i + 1}] : {item}")
    print('-' * 50)


def executar_acoes(item, estoque):

    if (item == 1):
        novo_estoque = comprar_fichas(estoque)

    return novo_estoque


def comprar_fichas(estoque):

    style.formatar_texto('CAIXA GERAL')
    print('Olá, eu sou o Caixa Geral!')
    quantidade = int(input('Quantas fichas deseja comprar? '))
    return estoque - quantidade