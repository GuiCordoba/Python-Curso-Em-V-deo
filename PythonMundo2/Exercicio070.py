'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre: A) qual é o total gasto na compra , B) quantos produtos custam mais de R$1000 e C) qual é o nome do produto mais barato.'''

print('-' * 40)
print(' ' * 11 + 'LOJA SUPER BARATÃO')
print('-' * 40)
maior = menor = total = maior_mil = count = 0
nome_menor = ' '
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    total += preco
    if preco > 1000:
        maior_mil += 1
    if count == 0 or preco < menor:
        menor = preco
        nome_menor = nome
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if op == 'N':
        break
    count += 1
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra é de R${total:.2f}.')
print(f'Temos {maior_mil} produtos custando mais que mil reais.')
print(f'O produto mais barato foi {nome_menor} e seu preço é R${menor:.2f}')
