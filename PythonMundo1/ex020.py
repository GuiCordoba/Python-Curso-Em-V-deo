import random
a1 = input('Informe o primeiro aluno: ')
a2 = input('Informe o segundo aluno: ')
a3 = input('Informe o terceiro aluno: ')
a4 = input('Informe o quarto aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentacao sera: {}'.format(lista))