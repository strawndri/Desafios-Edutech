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
    print(f' {"Total":<8} {"Ocupadas":<10} {"Preço":9} {"Categoria"}')

    for item in veiculos:
        for key, value in item.items():
            print(f'   {value[0]:<8} {value[1]:<8} R${value[2]:<7.2f} {key}')

    print('-' * 50)
    print(f'Caixa: R$ {caixa:.2f}')
    print('-' * 50)

def realizar_escolha():

    total, ocupadas = 0, 0

    while True:
        try:
            option = int(input('> Digite a opção desejada: '))
        except:
            option = int(input('> Tente novamente: '))

        if (option >= 1 and option <= 4):
            break

    for item in veiculos[option].values():
        total = item[0]
        ocupadas = item[1]

    if ocupadas >= total:
        print('Infelizmente estamos com todas as vagas ocupadas.')


# Programa ---------

# variáveis importantes do sistema

# A ordem da lista dos veículos é: total de vagas / vagas ocupadas / preço
veiculos = [
    {'Motos': [20, 0, 5.00]},
    {'Carros': [30, 0, 15.00]},
    {'Médio Porte': [20, 0, 20.00]},
    {'Grande Porte': [10, 0, 50.00]}]

caixa = 0

print_txt('Bem-vinda(o) ao nosso Estacionamento!', type='title')
menu()
realizar_escolha()
