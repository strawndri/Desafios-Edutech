from lib import acoes as ac, style
from time import sleep

estoque = 1000
fichas = 0
opcoes = ['Comprar fichas', 'Gastar fichas', 'Visualizar o estoque']
fechamento = ['Finalizar a festa', 'Continuar o programa', 'Nova pessoa']

style.formatar_texto('Bem vinda(o) à Festa da Escola!', tipo='especial')

while True:
    ac.apresentar_menu('Menu Inicial', opcoes)

    while True:
        try:
            opcao = int(input('> Escolha um dos itens acima: '))
        except ValueError:
            style.formatar_texto('ERRO')
            print('Tente novamente - ', end='')
        else:
            if(opcao > 0 and opcao <= 3):
                print(f'Opção escolhida: {opcoes[opcao - 1]}')
                sleep(1)
                break
            else:
                style.formatar_texto('O número digitado é inválido')
                print('Tente novamente - ', end='')


    estoque, fichas = ac.executar_acoes(opcao, estoque, fichas)
    print(estoque, fichas)
    ac.apresentar_menu('Menu de Finalização', fechamento)

    while True:
        try:
            opcao_f = int(input('> Escolha um dos itens acima: '))
        except ValueError:
            style.formatar_texto('ERRO')
            print('Tente novamente - ', end='')
        else:
            if(opcao_f > 0 and opcao_f <= 3):
                print(f'Opção escolhida: {fechamento[opcao_f - 1]}')
                sleep(1)
                break
            else:
                style.formatar_texto('O número digitado é inválido')
                print('Tente novamente - ', end='')

    if (opcao_f == 1):
        style.formatar_texto('Fim da festa', tipo='especial')
        break