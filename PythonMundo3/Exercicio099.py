'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from time import sleep
def maior(*numeros):
    count = maior = 0
    print('~' * 45)
    print('Analizando os valores passados...')
    for num in numeros:
        print(f'{num}', end=' ')
        sleep(0.5)
        if count == 0:
            maior = num
        else:
            if num > maior:
                maior = num
        count += 1
    print(f'. Foram informados {count} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    sleep(0.5)


maior(1, 2, 3)
maior(10, 2, 3)
maior(90)
maior()
print('~' * 45)
print('>>> PROGRAMA ENCERRADO <<<')