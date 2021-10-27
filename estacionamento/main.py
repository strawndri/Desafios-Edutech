# configurações de design
def print_txt(text, type='default'):

    if (type == 'title'):
        print('━' * 50)
        print(text.center(50))
        print('━' * 50)


# função que imprime menu
def menu():

    print('-' * 50)
    print_txt('Veículos', 'menu')
    print(f'{"Vagas":<6} {"Preço":7} {"Categoria"}')

    for item in veiculos:
        for key, value in item.items():
            print(f'{value[0]:<6} R${value[1]:<7} {key}')

    print('-' * 50)
    option = int(input('> Digite a opção desejada: '))
    return print(veiculos[option])

# Programa ---------

# variáveis importantes do sistema
vagas = {'disponiveis': 80, 'ocupadas': 0}

veiculos = [
    {'Motos': [20, 5.00]},
    {'Carros': [30, 15.00]},
    {'Médio Porte': [20, 20.00]},
    {'Grande Porte': [10, 50.00]}]


print_txt('Bem-vinda(o) ao nosso Estacionamento!', type='title')
menu()


