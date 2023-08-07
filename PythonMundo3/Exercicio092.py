'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import  datetime
funcionario = {}

funcionario['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
funcionario['idade'] = datetime.now().year - nascimento
funcionario['cpts'] = int(input('Carteira de trabalho (0 não tem): '))
if funcionario['cpts'] != 0:
    funcionario['contratação'] = int(input('Ano de contratação: '))
    funcionario['salario'] = int(input('Salário: R$'))
    ano_aposentadoria = funcionario['contratação'] + 35
    idade_aposentadoria = ano_aposentadoria - nascimento
    funcionario['aposentadoria'] = idade_aposentadoria

print('-' * 30)
for k, v in funcionario.items():
    print(f'- {k} tem o valor {v}')


