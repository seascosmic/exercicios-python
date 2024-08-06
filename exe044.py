produto = float(input('Qual o valor do produto: '))
pag = int(input('''Forma de pagamento: 
1.Dinheiro/cheque, 
2.À vista no cartão
3.Em até 2x
4.3x ou mais no cartão
Opção: '''))

if pag == 1:
    desconto = produto * 10 / 100
    print('O seu produto no valor de {:.2f} fica {:.2f} com 10% de desconto.'.format(produto, produto - desconto))
elif pag == 2:
    desconto = produto * 5 / 100
    print('O seu produto no valor de {:.2f} fica {:.2f} com 5% de desconto.'.format(produto, produto - desconto))
elif pag == 3:
    saldo = pag / 2
    print('Seu produto sai no valor normal de {} parcelado em 2x de {}.'.format(produto, saldo))
elif pag == 4:
    parcelas = int(input('Quantas parcelas: '))
    juros = produto + (produto * 20 / 100)
    divisao = juros / parcelas
    print('Seu produto de R${:.2f} parcelado em {}X de R${:.2f}. Com 20% de juros passa a ser R${:.2f} no total.'.format(produto, parcelas, divisao, juros))
