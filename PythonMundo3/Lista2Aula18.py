'''teste = list()
teste.append('Gui')
teste.append(30)
print(teste)
galera = list()
galera.append(teste[:])
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)'''

'''galera = [['João', 19], ['Ana', 33], ['Maria', 33]]
print(galera[1][0])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] <= 18:
        print(f'{p[0]} é maior de idade.')
        totmai =+ 1
    else:
        print(f'{p[0]} não é maior de idade.')
        totmen += 1
print(f'Temos {totmai} pessoas maiores de idade e {totmen} pessoas menores de idade.')