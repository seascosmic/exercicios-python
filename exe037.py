import math
numero = int(input('Digite um número: '))
base = int(input('''Digite o número para base de conversão: 
1.binário
2.octal
3.hexadecimal 
Sua opção: '''))
if base == 1:
    print('O número {} em binário fica {}.'.format(numero, bin(numero)))
elif base == 2:
    print('O número {} em octal é {}'.format(numero, oct(numero)))
elif base == 3:
    print('o número {} em hexadecimal é {}'.format(numero, hex(numero)))
else:
    print('Opção inválida. Tente novamente! <3')
