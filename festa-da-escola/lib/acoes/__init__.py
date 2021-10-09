from lib import style
from time import sleep

barracas = ['Cadeia', 'Correio Elegante', 'Churrasco',
                'Fliperama', 'Milho Verde', 'Morango',
                'Pebolim', 'Pipoca', 'Sonho', 'Tiro ao Alvo']

def apresentar_menu(titulo, list):

    style.formatar_texto(titulo, tipo='menu', cor='blue')
    for i, item in enumerate(list):
        print(f"[{i + 1}] : {item}")
    print('—' * 50)

def tratar_erro(list):
    while True:
        try:
            opcao = int(input('> Escolha um dos itens acima: '))
        except ValueError:
            style.formatar_texto('ERRO', cor='red')
            print('Tente novamente - ', end='')
        else:
            if(opcao > 0 and opcao <= 3):
                print(f'Opção escolhida: {list[opcao - 1]}')
                sleep(1)
                break
            else:
                style.formatar_texto('O número digitado é inválido', cor='red')
                print('Tente novamente - ', end='')

    return opcao

def executar_acoes(item, estoque, f):

    if (item == 1):
        novo_estoque, fichas = comprar_fichas(estoque, f)
    elif (item == 2):
        novo_estoque, fichas = gastar_fichas(estoque, f)
    elif (item == 3):
        novo_estoque, fichas = visualizar_estoque(estoque, f)

    return novo_estoque, fichas

def comprar_fichas(estoque, fichas):

    style.formatar_texto('CAIXA GERAL', cor='yellow')
    print('Olá, eu sou o Caixa Geral!')

    while True:
        quantidade = int(input('Quantas fichas deseja comprar? '))

        if (quantidade > 0 and quantidade <= estoque):
            break
        else:
            style.formatar_texto(f'Digite um valor válido para as {estoque} fichas do estoque!', cor='red')
            print('Tente Novamente -> ', end='')

    novo_estoque = estoque - quantidade
    fichas = quantidade + fichas

    return novo_estoque, fichas

def gastar_fichas(estoque, fichas):

    style.formatar_texto('CAIXA DE BARRACA', cor='yellow')

    if (fichas == 0):
        escolha = input('Você não possui fichas, deseja comprar? ').upper().split()[0]

        if escolha == 'S':
            novo_estoque, fichas = comprar_fichas(estoque, fichas)
        else:
            print('Finalizando processamento...')
            novo_estoque, fichas = 0, 0
    else:
        style.formatar_texto('Há diversas barracas que você pode ir: ', tipo='menu')
        apresentar_menu('Lista de Barracas disponíveis', barracas)

        while True:
            quantidade = int(input('Quantas fichas deseja gastar? '))

            if (quantidade > 0 and quantidade <= fichas):
                break
            else:
                print('Numero de fichas inválido.')
                print('Tente Novamente -> ', end='')

        novo_estoque = estoque + quantidade
        fichas = fichas - quantidade

    sleep(1)
    return novo_estoque, fichas

def visualizar_estoque(estoque, fichas):
    style.formatar_texto('ESTOQUE', cor='yellow')
    print(f'O total de fichas no estoque é: {estoque}')
    print(f'Você possui {fichas} fichas.')

    return estoque, fichas
