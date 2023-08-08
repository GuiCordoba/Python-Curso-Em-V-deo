'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area():
    a = float(input('LARGURA (m): '))
    b = float(input('COMPRIMENTO (m): '))
    area = a * b
    print(f'A aréa do seu terreno de {a} x {b} é {area} m2.')


print('Controle de Terrenos')
print('-' * 20)
area()