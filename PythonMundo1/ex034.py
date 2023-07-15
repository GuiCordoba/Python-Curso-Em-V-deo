salario = float(input('Qual o seu salario? R$'))
if salario > 1250:
    aumento = salario + (salario * 0.1)
else:
    aumento = salario + (salario * 0.15)
print('Seu novo salario sera R${}'.format(aumento))
