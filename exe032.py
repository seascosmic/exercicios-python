from datetime import date
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year #vai pegar apenas o ano da maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano {} é bissexto!'.format(ano))
else:
    print('Ano {} não é bissexto!'.format(ano))
