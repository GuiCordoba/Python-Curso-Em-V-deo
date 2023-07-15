nome = str(input('Informe o nome do atleta: '))
idade = int(input('Informe a idade do atleta: '))

if idade <=  9:
    categoria = "Mirim"
elif idade <=  14:
    categoria = "Infantil"
elif idade <=  19:
    categoria = "Juniors"
elif idade <=  20:
    categoria = "Senior"
else:
    categoria = "Master"

print('O aluno {} pertence a categoria: {}'.format(nome, categoria))