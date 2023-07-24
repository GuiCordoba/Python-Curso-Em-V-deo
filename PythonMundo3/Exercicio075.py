'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9, B) Em que posição foi digitado o primeiro valor 3 C) Quais foram os números pares.'''

numeros = (int(input('Informe um valor: ')), int(input('Informe outro valor: ')),
           int(input('Informe mais um valor: ')), int(input('Informe outro valor: ')),
            int(input('Informe o ultimo valor: ')))

print(f'Voce digitou os numeros: {numeros}')
print(f'o numero 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O numero 3 esta na posição {numeros.index(3) + 1}.')
else:
    print('O numero 3 não foi encontrado!')
print(f'Os numeros pares foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
