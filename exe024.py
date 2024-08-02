# cidade = str(input('Digite o nome da cidade: '))
# nome = cidade.find('santo')
# if nome == 0:
    #print('Começa com Santo, {}'.format(cidade))
# else:
#    print('Não começa com Santo, {}'.format(cidade))

cidade = str(input('Digite o nome da cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')