menor_peso = 0
maior_peso = 0
for c in range(1, 4):
    peso = float(input(f'Insira o peso da {c} pessoa: '))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso < menor_peso:
            menor_peso = peso
        if peso > maior_peso:
            maior_peso = peso

print(f'O maior peso inserido foi {maior_peso}kg.')
print(f'O menor peso inserido foi {menor_peso}kg.')