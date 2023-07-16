'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
pc = randint(0, 10)
print('Olá, sou seu computador. Acabei de pensar em um numero entre 0 e 10.')
print('Será que consegue adivinhar???.')
p = int(input('Qual o seu palpite? '))
palpites = 0
while p != pc:
    if p > pc:
        print('Menos... tente novamente!')
    if p < pc:
        print('Mais... tente novamente')
    p = int(input('Qual o seu palpite? '))
    palpites += 1
print(f'Acertou em {palpites} palpites. Parabens!')

