num = int(input('Digite um número: '))
u = num // 1 % 10 # está dividindo por um e tirando o
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('A unidade é {}'.format(u))
print('A dezena é {}'.format(d))
print('A centena é {}'.format(c))
print('O milhar é {}'.format(m))

