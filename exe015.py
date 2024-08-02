km = float(input('Quantos km foram percorridos? '))
dias = int(input('Quantos dias foi alugado? '))
preco = (dias * 60) + (km * 0.15)
print('O preço a ser pago é de R${}'.format(preco))