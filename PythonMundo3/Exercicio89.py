'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
 No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

from time import sleep
aluno = []
dados = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Nota 1: ')))
    dados.append(int(input('Nota 2: ')))
    media = (dados[1] + dados[2]) / 2
    dados.append(media)
    aluno.append(dados[:])
    dados.clear()
    op = str(input('Deseja continuar [S/N]? ')).upper()
    if op == 'N':
        break
print('-'*25)
print(f'{"No":<4}{"Nome":<10}{"Média":>8}')
print('-'*25)
for i, a in enumerate(aluno):
    print(f'{i:<4}{a[0]:<10}{a[3]:>8}')

while True:
    print('-' * 40)
    op = int(input('Mostar nota de qual aluno [999 para sair]: '))
    if op == 999:
        break
    if op <= len(aluno) - 1:
        print('-' * 40)
        print(f'As notas do aluno(a) {aluno[op][0]} são {aluno[op][1]} e {aluno[op][2]}.')

print('Finalizando...')
sleep(1)
print('Volte Sempre!!!')

