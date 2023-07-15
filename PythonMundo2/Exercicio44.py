preco = float(input('Informe o preço do produto: R$'))
pag = int(input('Qual a forma de pagamento?\n'
                      '[1] Dinheiro/Cheque.\n'
                      '[2] Á vista cartão.\n'
                      '[3] Até 2x no cartão.\n'
                      '[4] 3x ou mais no cartão.\n'
                      '--> '))
if pag == 1:
    total = preco - (preco * 0.10)
    print('Sua compra tem 10% de desconto. Total R${}'.format(total))
elif pag == 2:
    total = preco - (preco * 0.05)
    print('Sua compra tem 5% de desconto. Total R${}'.format(total))
elif pag == 3:
    total = preco
    print('Sua compra não tem desconto. Total R${}'.format(total))
elif pag == 4:
    total = preco + (preco * 0.20)
    print('Sua compra tem 20% de juros. Total R${}'.format(total))
else:
    print('Opção invalida!!')