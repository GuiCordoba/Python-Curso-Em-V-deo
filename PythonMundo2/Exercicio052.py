n = int(input("Insira um valor: "))
soma = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\33[33m', end=' ')
        soma += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO numero {n} foi divisivel {soma} vezes.')
if soma == 2:
    print("E por isso ele é primo!")
else:
    print("E por isso ele não é primo!!!")
