'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final,tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
dados = {}
gols = []
tot = 0
dados['nome'] = str(input('Nome: '))
part = int(input(f'Quantas partidas o {dados["nome"]} jogou? '))
for i in range(1, part+1):
    gols.append(int(input(f'    Quantos gols na partida {i}: ')))
dados['gols'] = gols[:]
dados['total'] = sum(gols)
print('-' * 40)
print(dados)
print('-' * 40)
for k, v in dados.items():
    print(f'o campo {k} tem o valor {v}.')
print('-' * 40)
print(f'O jogador {dados["nome"]} jogou {part} partidas:')
for k, v in enumerate (dados['gols']):
    print(f'   => Na partida {k+1}, fez {v} gols.')


