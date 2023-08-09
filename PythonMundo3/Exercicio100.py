'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
 e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''
from random import  randint
from time import sleep


def sorteio(lista):
    print('Sorteando 5 valores na lista: ', end=' ')
    for cont in range(0,5):
        n = randint(1, 10)
        numeros.append(n)
        print(f'{n}', end=' ')
        sleep(0.5)
    print('PRONTO!')


def somaPar(lista):
    sleep(1)
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    print(f'Somando os valores pares de {numeros}, temos {s}!')


numeros = []
sorteio(numeros)
somaPar(numeros)
