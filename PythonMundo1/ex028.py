'''import random
print('-' * 44)
n = int(input('De 0 a 5, em que numero estou pensando?? '))
lista = [0, 1, 2, 3, 4, 5]
aleatorio = random.choice(lista)
if n == aleatorio:
    print('Pensei no numero {}. Parabens, voce acertou!!'.format(aleatorio))
else:
    print('Pensei no numero {}. Tenten novamente!!'.format(aleatorio))
print('-' * 44)'''

from random import randint
from time import sleep
print('-' * 44)
jogador = int(input('De 0 a 5, em que numero estou pensando?? '))
pc = randint(0, 5)
print('Processando...')
sleep(2)
if jogador == pc:
    print('Pensei no numero {}. Parabens, voce acertou!!'.format(pc))
else:
    print('Pensei no numero {}. Tenten novamente!!'.format(pc))
print('-' * 44)