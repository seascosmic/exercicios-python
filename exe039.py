'''
como eu fiz:

from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))

if nasc == 2006:
    print('Você tem {} anos.'.format(atual-nasc))
    print('Deve se alistar imediatamente.')
elif nasc < 2006:
    print('Você tem {} anos em {}'.format((atual-nasc), atual))
    print('Você deveria ter se alistado há {} anos.'.format(2006-nasc))
elif nasc > 2006:
    print('Você tem {} anos.'.format(atual-nasc))
    print('Vai se alistar ainda. Faltam {} anos para o alistamento.'.format(nasc-2006))
'''
#correção
from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para se alistar.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('seu alistamento foi em {}.'.format(ano))
