op = str('')
soma = c = maior = menor = 0
while op != 'N':
    n = int(input('Digite um valor: '))
    if c == 0:
        maior = n
        menor = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    op = str(input('Deseja continuar [S/N]? ')).upper().strip()
    soma += n
    c += 1


media = soma / c
print(f'Você digitou {c} numeros e amédia entre eles é {media:.2f}.')
print(f'O menor valor entre eles foi {menor} e o maior foi {maior}.')