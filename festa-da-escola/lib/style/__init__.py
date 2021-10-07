def formatar_texto(txt, tipo='default'):

    if (tipo == 'default'):
        print('=' * 50)
        print(txt.center(50))
        print('=' * 50)
    elif (tipo == 'menu'):
        print(txt.center(50))
        print('-' * 50)