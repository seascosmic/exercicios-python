velocidade = int(input('Qual a sua velocidade: '))
if velocidade > 80:
    print('Você foi multado. a multa é R$ 7,00 por km acima.')
    print('O valor a ser pago é de R${}'.format((velocidade - 80) * 7))
