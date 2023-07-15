print('--------------Financiamento-------------')
valor = float(input('Informe o valor da casa: R$'))
anos = int(input('Em quantos anos pretende pagar a casa? '))
salario = float(input('Informe seu salario:'))

prestacao = valor / (anos * 12)
porsalario = salario * 0.15

if prestacao < porsalario:
    print('Parabens, emprestimo aprovado. Sua prestação sera de R${:.2f}.'.format(prestacao))
    print('Você pagara {} de R${:.2f}'.format(anos*12, prestacao))
else:
    print('Seu emprestimo não foi aprovado!!')