n = int(input('Digite um numero para ver sua tabuada: '))
print('Tabuada do {}:'.format(n))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, c*n))