'''Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:
A) Quantos números foram digitados, B) A lista de valores, ordenada de forma decrescente e C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = list()
s = 0
while True:
    lista.append(int(input('Insira um valor: ')))
    s += 1
    op = str(input('Deseja adicionar mais um valor [S/N]?  ')).upper()
    if op == 'N':
        break
lista.sort(reverse = True)
print('-+' * 25)
print(f'A lista em ordem decrescente é: {lista}.')
print(f'Foram inseridos {s} elementos na lista.')
if 5 in lista:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
print('-+' * 25)