from random import randint
from time import sleep
sorteio = randint(1,3)
jogador = int(input('''
Suas opções: 
1. PEDRA
2. PAPEL
3. TESOURA
Qual é a sua jogada? '''))
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(1)
if jogador == sorteio:
    print('Iguais, tente novamente.')
elif sorteio == 1 and jogador == 2:
    print('Tirei PEDRA e você PAPEL, você me ganhou!')
elif sorteio == 1 and jogador == 3:
    print('Eu tirei PEDRA e você TESOURA, GANHEI!')
elif sorteio == 2 and jogador == 1:
    print('Eu tirei PAPEL e você PEDRA, GANHEI!')
elif sorteio == 2 and jogador == 3:
    print('Eu tirei PAPEL e você tirou TESOURA, você GANHOU!')
elif sorteio == 3 and jogador == 1:
    print('Eu tirei TESOURA e você tirou PEDRA, você GANHOU!')
elif sorteio == 3 and jogador == 2:
    print('Eu tirei TESOURA e você tirou PAPEL, GANHEI!')
