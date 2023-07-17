'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
 O programa será interrompido quando o número solicitado for negativo.'''

while True:
    c = 0
    print('~' * 40)
    n = int(input('Deseja ver a tabuada de qual número: '))
    print('~' * 40)
    if n < 0:
        break
    while c <= 9:
        c += 1
        r = c * n
        print(f'{c} x {n} = {r}')

print('Programa de tabuada encerrado!')