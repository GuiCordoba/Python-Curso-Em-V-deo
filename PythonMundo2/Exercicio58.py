import time

def contagem():
    print('~~' * 20)
    print('Contagem de 1 até 10 de 1 em 1: ')
    for n in range(1 , 11):
        print(n, end=' ')
        time.sleep(0.3)
    print('~~' * 20)
    print('Contagem de 10 até 0 de 2 em 2: ')
    for n in range(10, 0, -2):
        print(n, end=' ')
        time.sleep(0.3)
    print('~~' * 20)
    print('Agora é sua vez, personalize a contagem: ')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    print('~~' * 20)
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio > fim:
        for n in range(inicio, fim+1, passo):
            print(n, end=' ')
            time.sleep(0.3)
        else:
            for n in range(inicio, fim-1, -passo):
                print(n, end=' ')
                time.sleep(0.3)
    print('~~' * 20)



contagem()




