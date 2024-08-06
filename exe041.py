from datetime import date
idade = int(input('Digite o seu ano de nascimento: '))
ano = date.today().year
if ano - idade <= 9:
    saldo = ano - idade
    print('Você tem {} anos.'.format(saldo))
    print('Classificação: MIRIM')
elif ano - idade <= 14:
    saldo = ano - idade
    print('Você tem {} anos.'.format(saldo))
    print('Classificação: INFANTIL')
elif ano - idade <= 19:
    saldo = ano - idade
    print('Você tem {} anos.'.format(saldo))
    print('Classificação: JÚNIOR')
elif ano - idade <=25:
    saldo = ano - idade
    print('Você tem {} anos.'.format(saldo))
    print('Classificação: SÊNIOR')
else:
    saldo = ano - idade
    print('Você tem {} anos.'.format(saldo))
    print('Classificação: MASTER')
