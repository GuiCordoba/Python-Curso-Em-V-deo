'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''

'''numeros = []
impar = []
par = []

for i in range(1, 8):
    n = int(input(f'Insira o {i}° valor: '))
    if n % 2 == 0:
        par.append(n)
        numeros.append(par)
    else:
        impar.append(n)
        numeros.append(impar)
numeros[1].sort()
numeros[0].sort()
print(f'Os valores pares digitados são: {numeros[1]}.')
print(f'Os valores impares digitados são: {numeros[0]}.')'''

numeros = [[],[]]
for i in range (1, 8):
    n = int(input(f'Insira o {i}o valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print('-' * 45)
print(f'Os valores pares digitados são: {numeros[0]}.')
print(f'Os valores impares digitados são: {numeros[1]}.')
