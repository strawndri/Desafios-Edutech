from lib import acoes as ac, style
from time import sleep

estoque = 1000
fichas = 0
opcoes = ['Comprar fichas', 'Gastar fichas', 'Visualizar o estoque',
          'Sair', 'Finalizar a festa']

style.formatar_texto('Bem vinda(o) à Festa da Escola!', tipo='especial', cor='purple')

while True:

    ac.apresentar_menu('Menu Inicial', opcoes)

    opcao = ac.tratar_erro(opcoes)

    if (opcao == 5):
        style.formatar_texto('Fim da festa', tipo='especial', cor='purple')
        sleep(2)
        break
    elif (opcao == 4):
        estoque = 1000
        fichas = 0

        style.formatar_texto('Obrigada por participar!', tipo='especial', cor='purple')
        print('Finalizando o programa e organizando o estoque...')
        sleep(2)

        print('\n' * 5)
        style.formatar_texto('Bem vinda(o) à Festa da Escola!', tipo='especial', cor='purple')
    else:
        estoque, fichas = ac.executar_acoes(opcao, estoque, fichas)




