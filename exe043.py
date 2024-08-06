peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('IMC {:.2f} - Abaixo do peso.'.format(imc))
elif 18.5 <= imc < 25:
    print('IMC {:.2f} - Peso ideal.'.format(imc))
elif 25 <= imc < 30:
    print('IMC {:.2f} - Sobrepeso.'.format(imc))
elif 30 <= imc <= 40:
    print('IMC {:.2f} - Obesidade'.format(imc))
else:
    ('IMC {:.2f} - Obesidade mórbida'.format(imc))
