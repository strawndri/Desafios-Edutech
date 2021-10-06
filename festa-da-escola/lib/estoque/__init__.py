from lib import style as s

def apresentarMenu(list):
    s.formatarTexto('MENU', type='menu_title')

    for i, item in enumerate(list):
        print(f'[{i + 1}] : {item}')
