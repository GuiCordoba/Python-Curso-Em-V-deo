def contador(i, f, p):
    '''
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem return
    Função criada por Guilherme Cordoba
    '''
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')


def somar(a=0, b=0, c=0):
    '''
    -> faz a soma de tres valores e mostra o resultado na tela
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    '''
    s = a + b + c
    return s


# help(contador)

r1 = somar(1)
r2 = somar(4, 9, 5)
r3 = somar(0, 7, 1)

print(f'Os resultados foram {r1}, {r2} e {r3}')