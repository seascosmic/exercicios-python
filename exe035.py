reta1 = float(input('Digite o comprimento da minha reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 and reta3 < reta1 + reta2:
    print('Os segmentos acima podem montar um triângulo!')
else:
    print('Os segmentos acima NÃO podem formar um triâangulo.')
