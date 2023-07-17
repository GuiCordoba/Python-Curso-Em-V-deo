'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while'''
print('Gerador de PA!')
primeiro_termo = int(input('Insira o primeiro termo: '))
razao = int(input('Razão da PA: '))
c = 0
termo = primeiro_termo

while c < 10:
    print(f'{termo} →' , end=' ')
    termo += razao
    c += 1
print('FIM!')
