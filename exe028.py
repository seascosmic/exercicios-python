import random
numero = int(input('Em que número eu pensei: '))
aleatorio = random.randint(0,5)
print(aleatorio)
if numero == aleatorio:
    print('Você venceu, PARABÉNS')
else:
    print('Você perdeu, tente novamente! Eu pensei em {}.'.format(aleatorio))
