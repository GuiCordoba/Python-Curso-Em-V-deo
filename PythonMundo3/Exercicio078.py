'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

valores = list()
for n in range(1, 6):
    valores.append(int(input(f'Insira um valor na posição {n}: ')))
print('-' * 45)
print('Valores inseridos: ', end='')
for n in valores:
    print(f'{n}', end=' ')
print(f'\nO maior valor da lista é {max(valores)}, na posição', end=' ')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}...', end=' ')
print()
print(f'O menor valor da lista é {min(valores)}, na posição', end=' ')
for i , v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...', end=' ')
print()
print('-' * 45)
