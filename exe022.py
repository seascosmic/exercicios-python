nome = str(input('Digite o seu nome: ')).strip()
print('Seu nome em maiúsculo é: '.format(nome.upper()))
print('Seu nome em minúsculo é: '.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))

