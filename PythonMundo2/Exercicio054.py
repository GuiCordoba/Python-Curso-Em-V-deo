from datetime import date
smaior = 0
smenor = 0
atual = date.today().year
for c in range (1, 8):
    ano = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    idade = atual - ano
    if idade >= 18:
        smaior += 1
    else:
        smenor += 1
print(f'Ao todo tivemos {smaior} pessoas maior de idade.')
print(f'E tambem {smenor} pessoas menores de idade.')