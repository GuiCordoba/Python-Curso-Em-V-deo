'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
 No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from time import sleep
from random import randint
from operator import itemgetter
jogo = {'jogador1' : randint(1,6),
        'jogador2' : randint(1,6),
        'jogador4' : randint(1,6),
        'jogador6' : randint(1,6)}

print('-' * 10 + 'Valores Sorteados' + '-' * 10)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
#o ranking sera uma lista pq apos ordernar se transforma em lista
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #o itemgetter faz com que seja ordenado pela key=1 que são os valores
print('-' * 12 + 'Ranlking' + '-' * 12)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar:  {v[0]} com {v[1]}.')
    sleep(1)