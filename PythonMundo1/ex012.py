p = float(input("Qual o preco do produto: "))
des = p - (p*0.05)
print('Valor do produto: R${}\nValor com desconto de 5%: R${:.2f}'.format(p, des))