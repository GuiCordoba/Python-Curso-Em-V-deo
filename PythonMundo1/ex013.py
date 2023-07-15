s = float(input("Qual o salario do funcionario: "))
a = s + (s*0.15)
print('Salario do funcionario: R${}\nNovo salario com aumento de 15%: R${:.2f}'.format(s, a))