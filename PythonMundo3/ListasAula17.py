'''num = [2, 3, 4, 5]
num [2] = 3
num.append(7)
num.sort(reverse=True)
num .insert(0, 1)
num.remove(3)
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

'''valores = []
valores.append(1)
valores.append(2)
valores.append(3)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Chegeui no final da lista.')'''

'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Chegeui no final da lista.')'''

a = [1, 2, 3, 4, 5]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')