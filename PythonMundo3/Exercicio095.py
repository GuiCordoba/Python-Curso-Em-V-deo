'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

time = []
jogador = {}
gols = []

while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(1, partidas+1):
        gols.append(int(input(f'  => Quantos gols na partida {p}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        op = str(input('Deseja continuar [S/N]: '))
        if op in 'SN':
            break
        print('ERRO! Insira somente S ou N.')
    if op == 'N':
        break
print('-=' * 17)
print(f'{"Cod":<3} {"Nome":>5} {"Gols":>12} {"Total":>10}')
print('-' * 33)
for k, v in enumerate(time):
    print(f'{k}', end=' ')
    for d in v.values():
        print(f'   {str(d):<8}', end=' ')
    print()
print('-=' * 17)
print()

while True:
    cod = int(input('Mostar dado de qual jogador [999 para sair]: '))
    if cod == 999:
        break
    if cod >= len(time):
        print(f'Não exite jogador com o código {cod}.')
    else:
        print(f'=> Levantamento do jogador {time[cod]["nome"]}')
        for i, g in enumerate(time[cod]["gols"]):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-=' * 17)
print('-=' * 17)
print('<<< Programa Encerrado >>>')