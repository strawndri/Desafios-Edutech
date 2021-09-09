grades = []
sum = 0
colors = {'none': '\033[01;m',
          'red': '\033[01;31m',
          'purple': '\033[01;35m'}

def message(text, color='none', line=False):
    print(colors[color])

    if line == True:
        print('✧----' * 12)
        print(text.center(65))
        print('✧----' * 12)
    else:
        print(text)

    print(colors['none'])



message('Média Escolar', 'purple', True)

for item in range(1, 5):

    while True:

        try:
            n = float(input(f' >   {item}ª Nota: '))
        except:
            message('--- [ERRO] Digite um valor válido.', 'red')
        else:
            if (n > 10 or n < 0):
                message('--- [ERRO] Digite um valor entre 0 e 10.', 'red')
            else:
                break

    grades.append(n)
    sum += n

if sum == 0:
    average = 0
    msg = 'Você foi reprovado(a). :('
else:
    average = sum / 4

    if ( 4 <= average < 6):
        msg = 'Você está de recuperação.'
    elif (average <= 3.9):
        msg = 'Você foi reprovado(a). :('
    else:
        msg = 'Você foi aprovado(a)! :)'

message('Resultado Final: ', 'purple', True)

for i, item in enumerate(grades):

    if (i == 0):
        print('| ', end='')

    print(item, end=' | ')
print(f'-> {average:.2f} ->', msg)



