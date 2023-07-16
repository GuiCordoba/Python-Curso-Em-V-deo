from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0

while op != 5:
    print('-' * 11, 'MENU', '-' * 11)
    print(''' [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] sair do programa''')
    op = int(input('---> Selecione uma opção: '))
    print('-' * 30)
    if op == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}.')
    elif op == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}.')
    elif op == 3:
        maior = 0
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior numero entre {n1} {n2} é {maior}.')

    elif op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção invalida! Tente novamente.')
    sleep(2)

print('-' * 30)
print('Até mais!')