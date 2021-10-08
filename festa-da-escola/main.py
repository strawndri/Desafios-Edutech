from lib import acoes as ac, style
from time import sleep

estoque = 1000
fichas = 0
opcoes = ['Comprar fichas', 'Gastar fichas', 'Visualizar o estoque']
fechamento = ['Finalizar a festa', 'Continuar o programa', 'Nova pessoa']

style.formatar_texto('Bem vinda(o) à Festa da Escola!', tipo='especial')

while True:
    ac.apresentar_menu('Menu Inicial', opcoes)

    opcao = ac.tratar_erro(opcoes)

    estoque, fichas = ac.executar_acoes(opcao, estoque, fichas)
    ac.apresentar_menu('Menu de Finalização', fechamento)

    opcao_f = ac.tratar_erro(fechamento)

    if (opcao_f == 1):
        style.formatar_texto('Fim da festa', tipo='especial')
        sleep(1)
        break
    elif (opcao_f == 3):
        estoque = 1000
        fichas = 0

        style.formatar_texto('Obrigada por participar!', tipo='especial')
        print('Finalizando o programa e organizando o estoque...')
        sleep(1)

        print('\n' * 3)
        style.formatar_texto('Bem vinda(o) à Festa da Escola!', tipo='especial')


