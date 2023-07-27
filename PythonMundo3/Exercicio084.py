'''Faça um programa que leia nome e peso de várias pessoas,uardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas, B) Uma listagem com as pessoas mais pesada e C) Uma listagem com as pessoas mais leves.'''

pessoas = list()
dados = list()
maiorpe = list()
menorpe = list()
count = maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso (kg):')))
    pessoas.append(dados[:])
    count += 1
    dados.clear()
    op = str(input('Deseja continuar [S/N]: ')).upper()
    if op == 'N':
        break
for p in pessoas:
    if p == 0:
        maiorpeso = p[1]
        menorpeso = p[1]
        maiorpe.append(p[0])
        maiorpe.append(p[0])
    else:
        if p[1] < menorpeso:
            menorpeso = p[1]
            maiorpe.append(p[0])
        if p[1] > maiorpeso:
            maiorpeso = p[1]
            maiorpe.append(p[0])
print(f'Foram cadastradas {count} pessoas.')
for p in maiorpe:
    print(f'O maior peso é {maiorpeso}. Peso de {maiorpe}')
for p in menorpe:
    print(f'O menor peso é {menorpeso}, Peso de {menorpe}')
print(f'Foram cadastradas {count} pessoas.')