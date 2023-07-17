'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('Gerador de PA!')
primeiro_termo = int(input('Insira o primeiro termo: '))
razao = int(input('Razão da PA: '))
c = 0
termo = primeiro_termo
mais = 10
total = 0

while mais != 0:
    total = total + mais
    while c <= total:
        print(f'{termo} →' , end=' ')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostar a mais?'))
print('FIM')
print(f'Progressão fonalizada com {total} termos impressos.')