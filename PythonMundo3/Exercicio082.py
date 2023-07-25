'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
 Ao final, mostre o conteúdo das três listas geradas.'''

valores = []
valores_par = []
valores_impar = []

while True:
    n = int(input('Insira um valor: '))
    valores.append(n)
    if n % 2 == 0:
        valores_par.append(n)
    else:
        valores_impar.append(n)
    op = str(input('Deseja continuar [S/N]: ')).upper()
    if op == 'N':
        break

valores.sort()
valores_impar.sort()
valores_par.sort()
print('*' * 30)
print(f'A lista completa é: {valores}.')
print(f'a lista de pares é: {valores_par}.')
print(f'a lista de imparess é: {valores_impar}.')
print('*' * 30)