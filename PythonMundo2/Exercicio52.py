n = int(input("Insira um valor: "))
soma = 0
for c in range(1, n):
    print(c)
    if n % 2 == 0:
        soma += 1

if soma == 2:
    print("Numero PRIMO!!!")
else:
    print("O numero não pe primo!")
