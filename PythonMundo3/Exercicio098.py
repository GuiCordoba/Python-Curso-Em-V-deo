'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada: a) de 1 até 10, de 1 em 1, b) de 10 até 0, de 2 em 2 e c) uma contagem personalizada'''

from  time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('~' * 30)
    print(f'Contando de {i} até {f} de {p} em {p}:')
    sleep(1)
    if i < f:
        for n in range(i, f+1, p):
            print(n, end=' ')
            sleep(0.25)
        print('FIM!')
    if i > f:
        for n in range(i, f-1, -p):
            print(n, end=' ')
            sleep(0.25)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('~' * 30)
print('Agora é sua vez. Informe os dados:')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
print('~' * 30)
print('>>> Programa Encerrado <<<')