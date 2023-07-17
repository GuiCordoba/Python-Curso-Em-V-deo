''' Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.'''
print('~' * 25)
print('SEQUENCIA DE FIBONACCI')
print('~' * 25)
n = int(input('Quantos termos voce quer mostrar? -> '))
t1 = 0
t2 = 1
print(f' {t1} → {t2} → ', end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(f'{t3} → ', end='')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')