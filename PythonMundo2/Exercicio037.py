n = int(input('Insira um numero inteiro qualquer: '))
base = int(input('Qual base deseja converter esse valor:\n[1] Binário.\n[2] Octal.\n[3] Hexadecimal.\n--> '))

if base == 1:
    print('Convertendo para Binário o numero {} é igual a: {}.'.format(n, bin(n)[2:]))
elif base == 2:
    print('Convertendo para Octal o numero {} é igual a: {}.'.format(n, oct(n)[2:]))
else:
    print('Convertendo para Hexadecimal o numero {} é igual a: {}.'.format(n, hex(n)[2:]))