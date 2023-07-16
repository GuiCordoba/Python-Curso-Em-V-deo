'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

soma_idade = 0
fem = 0
menor = 0
maior = 0
nome_maior = ''
for c in range(1, 5):
    print(f'---------- {c}° PESSOA ---------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo == 'F' and idade < 20:
        fem += 1
    if c == 1:
        maior = idade
        nome_maior = nome
    else:
        if sexo == 'Mn' and idade > maior:
            maior = idade
            nome_maior = nome
    soma_idade += idade



media_idade = soma_idade / c
print(f'A média de idade é {media_idade} anos.')
print(f'A pessoa mais velha tem {maior} anos de idade e se chama {nome_maior}.')
print(f'No total são {fem} mulheres menores de 20 anos.')
