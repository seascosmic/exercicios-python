casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Quantos anos vai ser pago? '))
prestacao = casa / (anos * 12)
valor = salario * 30 / 100
print('Para pagar a casa no valor de R${:.2f} a prestação sairá por R${:.2f}'.format(casa, prestacao))
if prestacao <= valor:
    print('Emprestímo concedido.')
else:
    print('Emprestimo negado.')
