from lib import acoes as ac, style

opcoes_gerais = ['Comprar fichas', 'Gastar fichas', 'Visualizar o estoque']


style.formatar_texto('Bem vinda(o) à Festa da Escola!')
ac.apresentar_menu(opcoes_gerais)

while True:
    try:
        opcao = int(input('> Escolha um dos itens acima: '))
    except ValueError:
        style.formatar_texto('ERRO')
        print('Tente novamente - ', end='')
    else:
        if(opcao > 0 and opcao <= 3):
            print(f'Opção escolhida: {opcoes_gerais[opcao - 1]}')
            break
        else:
            style.formatar_texto('O número digitado é inválido')
            print('Tente novamente - ', end='')


