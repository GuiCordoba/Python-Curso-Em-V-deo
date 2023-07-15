nome = str(input('Insira seu nome: '))
idade = int(input('Sua idade: '))
if idade > 18:
    print('Você já é maior de idade!!')
else:
    print('Voce ainda é menor de idade!')

if nome == "Guilherme":
    print('Que nome Lindo você tem!')
elif nome in 'Ana, Bia, Paula, Carina':
    print('Seu nome é muito bonito {}!'.format(nome))
else:
    print('Seu nome é bem normal!')
print('Muito prazer {}'.format(nome))