nota1 = float(input('Insira a 1o nota: '))
nota2 = float(input('Insira a 2o nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('Média menor que 5.0. REPROVADO!!')
elif media >= 5 and media <= 6.9:
    print('Média entre 5.0 e 6.90. RECUPERAÇÃO!!')
else:
    print('Média 7.0 ou superior. APROVADO!!')