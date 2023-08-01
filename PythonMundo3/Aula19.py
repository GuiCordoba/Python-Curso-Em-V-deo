'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade':26}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.values())
print(pessoas.keys())
for k, v in pessoas.items():
    print(f'{k} = {v}')'''
'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado1)

print(brasil[0]['uf'])
print(brasil[1]['Sigla'])'''

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla de Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()