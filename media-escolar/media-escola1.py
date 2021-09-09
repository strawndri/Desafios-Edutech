notas = []
soma = 0

def mensagem(texto):

    print('✧----' * 12)
    print(texto.center(64))
    print('✧----' * 12)


mensagem('Média Escolar')

for item in range(1, 5):

    while True:
        n = float(input(f' >   {item}ª Nota: '))

        if n >= 0 and n <= 10:
            break

    notas.append(n)
    soma += n


if soma == 0:
    media = 0
    msg = 'Você foi reprovado(a) :('
else:
    media = soma / 4

    if ( 4 <= media < 6):
        msg = 'Você está de recuperação.'
    elif (media <= 3.9):
        msg = 'Você foi reprovado(a) :('
    else:
        msg = 'Você foi aprovado(a)! :)'

mensagem('Resultado Final: ')

for i, item in enumerate(notas):

    if (i == 0):
        print('| ', end='')

    print(item, end=' | ')
print(f'-> {media:.2f} ->', msg)



