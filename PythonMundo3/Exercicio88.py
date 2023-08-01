'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e
 vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from time import  sleep
from random import randint
jogo = []
print('-' * 30)
print('      JOGA NA MEGA SENA     ')
print('-' * 30)
n = int(input('Quantos jogos serão gerados: '))
print('-'*8 + f' SORTEIO DE {n} JOGOS ' + '-'*8)
for i in range(1, n+1):
    for c in range(0, 6):
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    print(f'Jogo {i}: ', end=' ')
    jogo.sort()
    print(jogo)
    sleep(1)
    jogo.clear()

print('-'*12 + ' BOA SORTE! ' + '-'*12)

