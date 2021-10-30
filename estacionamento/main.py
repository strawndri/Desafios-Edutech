# configurações de design
def print_txt(text, type='default'):

    if (type == 'title'):
        print('━' * 50)
        print(text.center(50))
        print('━' * 50)


# função que imprime menu
def menu(type):

    print('-' * 50)

    if (type == 'principal'):
        print_txt('Veículos', 'menu')
        print(f' {"Total":<8} {"Ocupadas":<10} {"Preço":9} {"Categoria"}')

        for item in veiculos:
            for key, value in item.items():
                print(f'   {value[0]:<8} {value[1]:<8} R${value[2]:<7.2f} {key}')

        print('-' * 50)
        print(f'Caixa: R$ {caixa:.2f}')

    elif (type == 'pagamento'):

        for i, item in enumerate(op_pagamento):
            print(f'{i + 1} - {item}')

    elif (type == 'finalizacao'):

        for i, item in enumerate(itens_finalizacao):
            print(f'{i + 1} - {item}')

    print('-' * 50)

def realizar_escolha():

    total, indisponivel, i= 0, 0, 1

    while True:
        try:
            option = int(input('> Digite a opção desejada: '))
        except:
            option = int(input('> Tente novamente: '))

        if (option >= 1 and option <= 4):
            break

    for item in veiculos[option - 1].values():
        total = item[0]
        indisponivel = item[1]
        valor = item[2]

    if indisponivel >= total:
        print('Infelizmente estamos com todas as vagas ocupadas.')
    elif option == 1:
        print(f'Sua vaga é: {indisponivel + 1}')
    else:
        while i < option:
            for item in veiculos[i - 1].values():
                indisponivel += item[0]
            i += 1

        print(f'Sua vaga é: {indisponivel + 1}')
        print(f'Valor a pagar: R$ {valor}')

        menu('pagamento')

        op = int(input(f'> Opção escolhida: '))

        if (op == 1):
            resposta = True
        elif (op == 2):
            resposta = False
        elif (op == 3):
            sistema()

    return resposta, option


def pagamento(caixa, option):

    if (option == 1):
        caixa += 5
    elif (option == 2):
        caixa += 15
    elif (option == 3):
        caixa += 20
    else:
        caixa += 50

def sistema():
    print_txt('Bem-vinda(o) ao nosso Estacionamento!', type='title')
    menu('principal')
    resposta, option = realizar_escolha()
    print(resposta)
    if (resposta == True):
        pagamento(caixa, option)


# A ordem da lista dos veículos é: total de vagas / vagas ocupadas / preço
veiculos = [
    {'Motos': [20, 0, 5.00]},
    {'Carros': [30, 0, 15.00]},
    {'Médio Porte': [20, 0, 20.00]},
    {'Grande Porte': [10, 0, 50.00]}]

op_pagamento = ['Finalizar Pagamento', 'Cancelar Pagamento', 'Escolher outra opção']
itens_finalizacao = ['Continuar Sistema', 'Fechar estacionamento']

caixa = 0

while True:
    sistema()

    menu('finalizacao')
    opcao = int(input('> Opção Escolhida: '))

    if (opcao == 2):
        break


