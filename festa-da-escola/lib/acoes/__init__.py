from lib import style

def apresentar_menu(list):

    style.formatar_texto('Menu Principal', tipo='menu')
    for i, item in enumerate(list):
        print(f"[{i + 1}] : {item}")
    print('-' * 50)

