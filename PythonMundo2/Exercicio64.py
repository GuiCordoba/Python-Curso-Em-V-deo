cont = soma = n = 0
while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    if n != 999:
        soma += n
    cont += 1

print(f'Você digitou {cont - 1} numeros e a soma deles é {soma}.')