frase = str(input('Insira uma frase: ')).strip().upper()
palavras = frase.split() #separa a frase por palavras
junto = ''.join(palavras) #elimina os espaços internos entre as palavras
#inverso = ''

'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''

inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('Não temos um palindromo!')