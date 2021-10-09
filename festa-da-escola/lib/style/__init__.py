def formatar_texto(txt, tipo='default', cor='default'):

    colors = {
        'default': '\033[01m',
        'red': '\033[01;31m',
        'yellow': '\033[01;33m',
        'purple': '\033[01;35m',
        'blue': '\033[01;36m'
    }

    print(colors[cor], end='')

    if (tipo == 'default'):
        print('=' * 60)
        print(txt.center(60))
        print('=' * 60, colors['default'])
    elif (tipo == 'menu'):
        print(colors[cor], end='')
        print('—' * 60)
        print(txt.center(60))
        print('—' * 60, colors['default'])
    elif (tipo == 'especial'):
        print('━' * 60)
        print(txt.upper().center(60))
        print('━' * 60, colors['default'])
