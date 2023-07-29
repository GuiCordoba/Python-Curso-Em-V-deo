'''Faça um programa que leia nome e peso de várias pessoas,uardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas, B) Uma listagem com as pessoas mais pesada e C) Uma listagem com as pessoas mais leves.'''

pessoas = list()
dados = list()
count = maiorpeso = menorpeso  = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso (kg):')))
    if len(pessoas) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    op = str(input('Deseja continuar [S/N]: ')).upper()
    if op == 'N':
        break


print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso é {maiorpeso}. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso é {menorpeso}, Peso de ', end='')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'[{p[0]}]', end=' ')
