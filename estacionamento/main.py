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

    print('\n', end='')
    print('—' * 50)
    print_txt(type, 'title_menu')

    if (type == 'principal'):
        print_txt('Veículos', 'menu')
        print(f'  {"N°":<4} {"Total":<7} {"Ocupadas":<10} {"Preço":9} {"Categoria"}')

        # tabela listando os veículos, suas vagas e preços
        for i, item in enumerate(veiculos):
            print(f'  {i + 1:<6}', end='')
            for key, value in item.items():
                print(f'{value[0]:<9} {value[1]:<7} R${value[2]:<7.2f} {key}')

        print('-' * 50)
        print(f'Caixa: R$ {sum(caixa):.2f}')

    elif (type == 'pagamento'):
        for i, item in enumerate(op_pagamento):
            print(f'{i + 1} - {item}')

    elif (type == 'finalização'):
        for i, item in enumerate(itens_finalizacao):
            print(f'{i + 1} - {item}')

    elif (type == 'resultado final'):
        print(f'{"":<10} {"Total de Veículos":<20} {"Caixa"}')

        total_ocupadas = 0
        for i, item in enumerate(veiculos):
            valor_estacionamento = caixa[i]
            for key, value in item.items():
                total_ocupadas += value[3]
                print(f'{"":<10} {value[3]} - {key:<16} R$ {valor_estacionamento:.2f}')

        print(f'{"-" * 30}'.center(50))
        print(f'{"":<10} {total_ocupadas} - Veículos {" ":<7} R$ {sum(caixa):.2f}')

    print('—' * 50)


# função que exige o número correto a ser digitado
def tratamento_valor(list):
    while True:
        try:
            option = int(input('> Digite a opção desejada: '))
        except ValueError:
           print(' ┈ ┈ (!) Tente novamente: valor inválido (!) ┈ ┈ ')
        else:
            if (option >= 1 and option <= len(list)):
                break
            else:
                print(f' ┈ ┈ (!) O valor precisa ser entre 1 e {len(list)} (!) ┈ ┈ ')

    return option

# função que realiza o pagamento do estacionamento
def pagamento(caixa, option):

    for item in veiculos[option - 1].values():
        valor_estacionamento = item[2]

    return valor_estacionamento


#função principal
def cadastrar_vaga():

    menu('principal')
    total, indisponivel, i = 0, 0, 1

    option = tratamento_valor(veiculos)


    #salva o total de vagas, as indisponíveis e o valor a pagar
    for item in veiculos[option - 1].values():
        total = item[0]
        indisponivel = item[1]
        valor = item[2]

        print(total, indisponivel)

    vaga = indisponivel + 1

    #computando a vaga no sistema
    if indisponivel >= total:
        print('Infelizmente estamos com todas as vagas ocupadas.')
        valor = 0
    elif option == 1:
        print(f'Sua vaga é: {vaga}')
    else:
        while i < option:
            for item in veiculos[i - 1].values():
                indisponivel += item[0]
            i += 1

        vaga = indisponivel + 1
        print(f'Sua vaga é: {vaga}')

    print(f'Valor a pagar: R$ {valor:.2f}')
    menu('pagamento')

    option2 = tratamento_valor(op_pagamento)

    if (option2 == 1):
        # organiza as vagas ocupadas e o total do dia
        for item in veiculos[option - 1].values():
            item[1] = item[1] + 1
            item[3] = item[3] + 1
        resposta = True # cliente confirmou o pagamento

    elif (option2 == 2):
        resposta = False # cliente cancelou o pagamento

    elif (option2 == 3):
        cadastrar_vaga() # cliente optou por outra classificação

    return resposta, option, vaga


# A ordem da lista dos veículos é: total de vagas / vagas ocupadas / preço / entrada de veiculos
veiculos = [
    {'Motos': [20, 0, 5.00, 0]},
    {'Carros': [30, 0, 15.00, 0]},
    {'Médio Porte': [20, 0, 20.00, 0]},
    {'Grande Porte': [10, 0, 50.00, 0]}]

op_pagamento = ['Finalizar Pagamento', 'Cancelar Pagamento', 'Escolher outra opção']
itens_finalizacao = ['Continuar Sistema', 'Remover vaga', 'Fechar estacionamento']
caixa = [0, 0, 0, 0]
total_ocupadas = 0

while True:

    print_txt('Bem-vinda(o) ao nosso Estacionamento!', type='title')
    resposta, option, vaga = cadastrar_vaga()

    # adiciona o pagamento ao caixa
    if (resposta == True):
        caixa[option - 1] += pagamento(caixa, option)

    # processamento cancelado
    elif (resposta == False):
        break

    sleep(1)

    # finalicação do programa
    menu('finalização')
    option3 = tratamento_valor(itens_finalizacao)

    sleep(1)

    # remove a vaga atual
    if (option3 == 2):
        for item in veiculos[option - 1].values():
            item[1] = item[1] - 1
            print(f'Liberando a vaga {vaga}...')

    # finaliza o programa e apresenta o resultado final do dia
    elif (option3 == 3):
        for item in veiculos:
            for i in item.values():
                total_ocupadas += i[1]

        menu('resultado final')
        break

print_txt('Obrigada por utilizar o nosso serviço!', type='title')


