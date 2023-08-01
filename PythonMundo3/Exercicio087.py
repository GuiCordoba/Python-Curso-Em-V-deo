'''Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados,
B) A soma dos valores da terceira coluna e C) O maior valor da segunda linha.'''

matriz = [[0,0,0], [0,0,0], [0,0,0]]
pares = count = soma_coluna = maior = 0
'''for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Insira um valor para [{l}, {c}]: '))
        #Soma dos pares
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        #Soma da terceira coluna
        if matriz[l][2]:
            soma_coluna += matriz[l][c]
        #Maior da segunda linha
        if matriz[1][c]:
            if c == 4:
                maior = matriz[1][c]
            elif matriz[l][c] > maior:
                maior = matriz[1][c]'''

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Insira um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^4} ]', end=' ')
        #Soma dos pares
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print()

print('-'* 40)
print(f'A soma dos valores pares digitados é {pares}.')
#Soma da terceira coluna
for l in range(0, 3):
    soma_coluna =+ matriz[l][2]
print(f'A soma da terceira coluna é {soma_coluna}.')
#Maior da segunda linha
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}.')
print('-'* 40)