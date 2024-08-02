prod = float(input('Digite o preço do produto: R$'))
p =  prod - (prod * 5 / 100)
print('O produto de valor R${:.2f}, com 5% de desconto fica R${:.2f}.'.format(prod, p))
