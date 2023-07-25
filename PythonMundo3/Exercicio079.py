'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
numeros = list()

while True:
    n = int(input('Insira um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado. Não adicionado na lista...')

    op = str(input('Deseja continuar [S/N]: ')).upper()
    while True:
        if op not in 'SN':
            op = str(input('Ops... Tente novammente [S/N]:')).upper()
        else:
            break
    if op == 'N':
        break
numeros.sort()
print(f'Os valores digitados foram: {numeros}')