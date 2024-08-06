reta1 = float(input('Digite a priemira medida: '))
reta2 = float(input('Digite a segunda medida: '))
reta3 = float(input('Digite a segunda medida: '))
if reta1 < reta2 + reta3 and reta2 < reta1 and reta3 < reta1 + reta2:
    print('Os segmentos acima podem montar um triângulo ', end='')
    if reta1 != reta2 != reta3 != reta1:
        print('ESCALENO')
    elif reta1 == reta2 == reta3:
        print('EQUILÁTERO')
    else:
        print('ISÓSCELES')
else:
    ('Não forma triângulo.')
