nome = str(input('Informe seu nome completo: ')).strip()
div = nome.split()
print('Primeiro nome: {}'.format(div[0]))
print('Ultimo nome: {}'.format(div[len(div) - 1]))