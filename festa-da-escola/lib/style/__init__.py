def formatarTexto(txt, type='default'):

    if (type == 'default'):
       print(txt)
    elif (type == 'title'):
        print('=' * 50)
        print(txt.upper().center(50))
        print('=' * 50)
    elif (type == 'menu_title'):
        print(txt.upper().center(50))
        print('-' * 50)



