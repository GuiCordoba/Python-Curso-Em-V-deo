d = int(input('Por quantos dias o carro ficou alugado: '))
km = int(input('Quantos km foi rodado: '))
preco = (60 * d) + (km * 0.15)
print('O valor total do aluguel ficou: R${}'.format(preco))