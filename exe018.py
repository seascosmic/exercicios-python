import math
ang = int(input('Digite um angulo: '))
tan = math.tan(math.radians(ang))
cos = math.cos(math.radians(ang))
seno = math.sin(math.radians(ang))
print('A tangente é {:.3f}, cosseno é {:.3f} e o seno é {:.3f}'.format(tan, cos, seno))


