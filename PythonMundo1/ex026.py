frase = str(input('Insira uma frase qualquer: ')).strip().lower()
print('Numero de vezes que aparece a letra "a": {}'.format(frase.count('a')))
print('A priemira letra "a" aparrece na posicao {}'.format(frase.find('a')+1))
print('A ultima letra a apareceu na posicao {}'.format(frase.rfind('a')+1))
