salario = float(input('Digite o seu salário: R$'))
if salario <= 1200:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Se seu salário era de {:.2f} você passou a ganhar {:.2f} agora.'.format(salario, novo))
