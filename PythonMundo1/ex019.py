import random
a1 = input('Informe o primeiro aluno: ')
a2 = input('Informe o segundo aluno: ')
a3 = input('Informe o terceiro aluno: ')
a4 = input('Informe o quarto aluno: ')
a5 = input('Informe o quinto aluno: ')
lista = [a1,a2, a3, a4, a5]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))