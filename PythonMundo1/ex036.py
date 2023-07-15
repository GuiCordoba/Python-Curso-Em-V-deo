'''a = 19 % 2
print(a)'''
entrada = input().split()

'''distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

imc = distancia / (diametro1 + diametro2)

print(imc)'''

valores = input().split()
total_cachorro_quente = int(valores[0])
total_participantes = int(valores[1])

media = total_cachorro_quente / total_participantes

print(f'{round(media,2)}')