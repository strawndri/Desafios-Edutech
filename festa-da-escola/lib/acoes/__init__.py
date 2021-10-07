from lib import style

barracas = ['Cadeia', 'Correio Elegante', 'Churrasco',
                'Fliperama', 'Milho Verde', 'Morango',
                'Pebolim', 'Pipoca', 'Sonho', 'Tiro ao Alvo']

def apresentar_menu(list):

    style.formatar_texto('Menu Principal', tipo='menu')
    for i, item in enumerate(list):
        print(f"[{i + 1}] : {item}")
    print('-' * 50)


def executar_acoes(item, estoque, f):

    if (item == 1):
        novo_estoque, fichas = comprar_fichas(estoque, f)
    elif (item == 2):
        novo_estoque, fichas = gastar_fichas(estoque, f)

    return novo_estoque, fichas


def comprar_fichas(estoque, fichas):

    style.formatar_texto('CAIXA GERAL')
    print('Olá, eu sou o Caixa Geral!')
    quantidade = int(input('Quantas fichas deseja comprar? '))
    return (estoque - quantidade), (quantidade + fichas)

def gastar_fichas(estoque, fichas):

    if (fichas == 0):
        escolha = input('Você não possui fichas, deseja comprar? ').upper().split()[0]
        if escolha == 'S':
            comprar_fichas(estoque, fichas)
        else:
            print('ok')


    style.formatar_texto('CAIXA DE BARRACA')
    style.formatar_texto('Há diversas barracas que você pode ir: ', tipo='menu')
    apresentar_menu(barracas)

    quantidade = int(input('Quantas fichas deseja gastar? '))
    return estoque + quantidade, fichas - quantidade
