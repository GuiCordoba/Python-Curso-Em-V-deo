valorHamburguer = 10
quantidadeHamburguer = 2
valorBebida = 5
quantidadeBebida = 1
valorPago = 30


precoFinal = (valorHamburguer * quantidadeHamburguer) + (valorBebida * quantidadeBebida)

troco = valorPago - precoFinal

print(f'O preço final do pedido é R$ {precoFinal:.2f}. Seu troco é R$ {troco:.2f}.')
