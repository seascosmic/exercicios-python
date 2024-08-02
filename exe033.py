numeroUm = int(input('Digite o primeiro número: '))
numeroDois = int(input('Digite o segundo numero: '))
numeroTres = int(input('Digite o terceiro número: '))
menor = numeroUm
if numeroUm > numeroDois and numeroDois < numeroTres:
    menor = numeroDois
if numeroTres < numeroUm and numeroTres < numeroDois:
    menor = numeroTres
maior = numeroUm
if numeroDois > numeroUm and numeroDois > numeroTres:
    maior = numeroDois
if numeroTres > numeroDois and numeroTres > numeroUm:
    maior = numeroTres
print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))
