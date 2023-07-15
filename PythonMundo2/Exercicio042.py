print('-'* 25)
print('>Formando um triangulo<')
print('-'* 25)
a = int(input('Informe a primeira reta: '))
b = int (input('Informe a segunda reta: '))
c = int(input('Informe a terceira reta: '))
if (a < b + c) and (b < a + b) and (c < a + b):
    print('E possivel formar um triangulo!')
    if (a == b == c):
        print('E o triangulo é Equilatéro!')
    elif (a == b) or (a == c) or (b == c):
        print('Triangulo Isóceles!!')
    else:
        print('Triangulo Escaleno!')

else:
    print('Não é possivel formar um triangulo!')