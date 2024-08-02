viagem = float(input('Qual a distância da sua viagem em km? ')).strip()
duzentos = viagem * 0.50
acima = viagem * 0.45
if viagem <= 200:
    print('Valor de R${:.2f} com taxa de R$ 0,50 reais por km.'.format(duzentos))
else:
    print('O valor da viagem saiu por R${:.2f} com a taxa de R$0.45 reais por km.'.format(acima))
