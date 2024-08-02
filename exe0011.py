larg = float(input('Qual a largura da sua parede: '))
alt = float(input('Qual a altura da sua parede: '))
a = larg * alt
print('Sua parede tem dimensão de {}x{} e sua área é de {}.'.format(larg, alt, a))
tinta = a / 2
print('Para pintar a area de {}, você precisará de {}L de tinta'.format(a, tinta))
