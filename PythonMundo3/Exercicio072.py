'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
 Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
numeros = ('Zero','Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')


while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if num >= 0 and num <= 20:
        op = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
        if op == 'N':
            break
    print('Tente novamente. ', end='')

print(f'Voce digitou o numero {numeros[num]}. ')
