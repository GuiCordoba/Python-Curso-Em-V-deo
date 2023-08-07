'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
 A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média'''

lista = []
dicionario ={}
op = ' '
soma_idade =  tot = 0
while True:
    dicionario.clear()
    dicionario['nome'] = str(input('Nome: '))
    #Validação do sexo
    while True:
        dicionario['sexo'] = str(input('Sexo: '))
        if dicionario['sexo'] in 'FM':
            break
        print('Por favor, insira apenas F ou M!')

    dicionario['idade'] = int(input('Idade: '))
    soma_idade += dicionario['idade']

    lista.append(dicionario.copy())

    #validação da opção deseja continuar
    while True:
        op = str(input('Deseja continuar [S/N]: '))
        if op in 'SN':
            break
        print('Por favor, insira apenas S ou N')
    if op == "N":
        break

print(f'A) Foram cadastradas {len(lista)} pessoas.')
media = soma_idade / len(lista)
print(f'B) A média de idades das pessoas é {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] == "F":
        print(f'{p["nome"]}', end=' ')
print()
print('D) Lista de pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] > media:
        print(f'nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]}. ')
print('ENCERRADO!!')

