print('-'* 25)
print('>Formando um triangulo<')
print('-'* 25)
a = int(input('Informe a primeira reta: '))
b = int (input('Informe a segunda reta: '))
c = int(input('Informe a terceira reta: '))
if (a < b + c) and (b < a + b) and (c < a + b):
    print('E possivel formar um triangulo!')
else:
    print('Nao e possivel formar um triangulo!')
