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
    print(estoque, fichas)
    ac.apresentar_menu('Menu de Finalização', fechamento)

    opcao_f = ac.tratar_erro(fechamento)

    if (opcao_f == 1):
        style.formatar_texto('Fim da festa', tipo='especial')
        break