frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vez(es)'.format(frase.count("A")))
print('A posição da letra A é {}'.format(frase.find("A")+1))
print('A sua última posição é {}'.format(frase.rfind("A")+1))
