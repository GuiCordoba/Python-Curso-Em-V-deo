'''Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''

'''parte1 = []
parte2 = []
parte3 = []

for i in range(0, 3):
    parte1.append(int(input(f'Insira um valor para [0, {i}]: ')))

for i in range(0, 3):
    parte2.append(int(input(f'Insira um valor para [1, {i}]: ')))

for i in range(0, 3):
    parte3.append(int(input(f'Insira um valor para [2, {i}]: ')))

print('-'* 25)
for n in parte1:
    print(f'[ {n:^3} ]', end='')
print()
for n in parte2:
    print(f'[ {n:^3} ]', end='')
print()
for n in parte3:
    print(f'[ {n:^3} ]', end='')
print()
print('-'* 25)'''

#Uma solução melhor
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-' * 25)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^4} ]', end=' ')
    print()
print('-' * 25)