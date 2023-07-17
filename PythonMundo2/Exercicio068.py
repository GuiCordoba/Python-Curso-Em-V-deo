'''Faça um programa que jogue par ou ímpar com o computador.
 O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo'''
from random import randint
pc = randint(1, 10)
vitoria = 0
print('VAMOS JOGAR PAR OU IMPAR')
while True:
    jogador = int(input('Diga um valor: '))
    par_impar = str(input('Par ou Impar [P/I]: ')).upper().strip()
    soma = jogador + pc
    print(f'->Você jogou {jogador} e o computador {pc}. Total de {soma}.', end=' ')
    print('Deu PAR!' if soma % 2 == 0 else 'Deu IMPAR!')
    if soma % 2 == 0 and par_impar == 'P':
        print('=-=' * 20)
        print('->Você VENCEU!!')
        print('=-=' * 20)
        vitoria += 1
    elif soma % 2 != 0 and par_impar == 'I':
        print('=-=' * 20)
        print('->Você VENCEU!!')
        print('=-=' * 20)
        vitoria += 1
    else:
        print('=-=' * 20)
        print('->Você PERDEU!!')
        break
    print('-> Vamos jogar novamente...')
print('=-='* 20)
print(f'GAME OVER. Você ganhou {vitoria} vezes.')
print('=-='* 20)

