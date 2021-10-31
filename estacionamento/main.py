from time import sleep

# configurações de design
def print_txt(text, type='default'):

    if (type == 'title'):
        print('━' * 50)
        print(text.center(50))
        print('━' * 50)
    elif (type == 'title_menu'):
        print(text.center(50).upper())
        print(f'{"-" * 40}'.center(50))


# função que imprime menu
def menu(type):

    print('-' * 50)
    print_txt(type, 'title_menu')

    if (type == 'principal'):
        print_txt('Veículos', 'menu')
        print(f'  {"N°":<4} {"Total":<7} {"Ocupadas":<10} {"Preço":9} {"Categoria"}')

        for i, item in enumerate(veiculos):
            print(f'  {i + 1:<6}', end='')
            for key, value in item.items():
                print(f'{value[0]:<9} {value[1]:<7} R${value[2]:<7.2f} {key}')

        print('-' * 50)
        print(f'Caixa: R$ {caixa:.2f}')

    elif (type == 'pagamento'):

        for i, item in enumerate(op_pagamento):
            print(f'{i + 1} - {item}')

    elif (type == 'finalizacao'):

        for i, item in enumerate(itens_finalizacao):
            print(f'{i + 1} - {item}')

    elif (type == 'resultado final'):
        print(f'{"":<10} {"Total de Veículos":<20} {"Caixa"}')

        total_ocupadas = 0
        for item in veiculos:
            for key, value in item.items():
                total_ocupadas += value[3]
                print(f'{"":<10} {value[3]} - {key:<16} R$ {value[2]:.2f}')

        print(f'{"-" * 30}'.center(50))
        print(f'{"":<10} {total_ocupadas} - Veículos {" ":<7} R$ {caixa:.2f}')

    print('-' * 50)


# função que exige o número correto a ser digitado
def tratamento_valor(list):
    while True:
        try:
            option = int(input('> Digite a opção desejada: '))
        except ValueError:
           print('Tente novamente: ', end='')
        else:
            if (option >= 1 and option <= len(list)):
                break
            else:
                print(f'O valor precisa ser entre 1 e {len(list)}')

    return option

def pagamento(caixa, option):

    for item in veiculos[option - 1].values():
        caixa = item[2]

    return caixa


#função principal
def sistema():
    menu('principal')
    total, indisponivel, i = 0, 0, 1

    option = tratamento_valor(veiculos)

    for item in veiculos[option - 1].values():
        total = item[0]
        indisponivel = item[1]
        valor = item[2]

        print(total, indisponivel)

    #computando a vaga no sistema
    if indisponivel >= total:
        print('Infelizmente estamos com todas as vagas ocupadas.')
        valor = 0
    elif option == 1:
        print(f'Sua vaga é: {indisponivel + 1}')
    else:
        while i < option:
            for item in veiculos[i - 1].values():
                indisponivel += item[0]
            i += 1

        print(f'Sua vaga é: {indisponivel + 1}')

    print(f'Valor a pagar: R$ {valor:.2f}')
    menu('pagamento')

    option2 = tratamento_valor(op_pagamento)

    if (option2 == 1):
        for item in veiculos[option - 1].values():
            item[1] = item[1] + 1
            item[3] = item[3] + 1
        resposta = True
    elif (option2 == 2):
        resposta = False
    elif (option2 == 3):
        sistema()

    return resposta, option


# A ordem da lista dos veículos é: total de vagas / vagas ocupadas / preço / entrada de veiculos
veiculos = [
    {'Motos': [20, 0, 5.00, 0]},
    {'Carros': [30, 0, 15.00, 0]},
    {'Médio Porte': [20, 0, 20.00, 0]},
    {'Grande Porte': [10, 0, 50.00, 0]}]

op_pagamento = ['Finalizar Pagamento', 'Cancelar Pagamento', 'Escolher outra opção']
itens_finalizacao = ['Continuar Sistema', 'Remover vaga', 'Fechar estacionamento']
caixa = 0
total_ocupadas = 0

while True:

    print_txt('Bem-vinda(o) ao nosso Estacionamento!', type='title')
    resposta, option = sistema()

    if (resposta == True):
        caixa += pagamento(caixa, option)
    elif (resposta == False):
        break

    sleep(1)

    menu('finalizacao')
    option3 = tratamento_valor(itens_finalizacao)

    sleep(1)

    if (option == 2):
        for item in veiculos[option - 1].values():
            print('entrou op 2')
            item[1] = item[1] - 1

    elif (option3 == 3):

        for item in veiculos:
            for i in item.values():
                total_ocupadas += i[1]

        menu('resultado final')
        break


