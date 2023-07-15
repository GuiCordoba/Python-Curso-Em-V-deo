dist = float(input('Qual a distancia da viagem (km): '))
'''if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45'''
preco = dist * 0.50 if dist <= 200 else dist * 0.45
print('Valor da viagem: R${:.2f}'.format(preco))
print('Boa viagem!')