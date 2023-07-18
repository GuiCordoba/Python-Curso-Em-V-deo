'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos,
B) quantos homens foram cadastrados e C) quantas mulheres tem menos de 20 anos.'''
total_maior = total_homens = total_mulheres = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input("Idade: "))
    if idade > 18:
        total_maior += 1
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        total_mulheres += 1
    print('-' * 30)
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar [S/N] ? ')).upper().strip()[0]
    if op == 'N':
        break
print('-'*45)
print(f'{total_maior} pessoas tem mais de 18 anos.')
print(f'Foram cadastrados {total_homens} homens.')
print(f'{total_mulheres} mulheres tem menos de 20 anos de idade.')
print('-'*45)