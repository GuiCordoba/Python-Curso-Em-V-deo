'''Faça um programa que leia um número qualquer e mostre o seu fatorial.'''
n = int(input('Insira um valor para o calculo de seu fatorial: '))
c = n
fat = 1
print(f'Calculando {n}! -> ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat *= c
    c -= 1
print(fat)

