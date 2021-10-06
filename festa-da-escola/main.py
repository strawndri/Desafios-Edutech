from lib import style as s
from lib import estoque as e


s.formatarTexto('Bem-Vinda(o) à Festa Escolar!', type='title')
op = e.apresentarMenu()

try:
    int(op)
except ValueError:
   print('erro')