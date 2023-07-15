salario = float(input())


def mostar_mensagem(novo_salario, reajuste, percentual):
    print(f"Novo salario: {format(novo_salario, '.2f')}\nReajuste ganho: {format(reajuste, '.2f')}\nEm percentual: {percentual}")


def calculo_salario(salario):
    if (salario > 0 and salario <= 600):
        reajuste = salario * 0.17
        percentual = '17%'
    elif (salario > 600 and salario <= 900):
        reajuste = salario * 0.13
        percentual = '13%'

    elif (salario > 900 and salario <= 1500):
        reajuste = salario * 0.12
        percentual = '12%'

    elif (salario > 1500 and salario <= 2000):
        reajuste = salario * 0.10
        percentual = '10%'

    else:
        reajuste = salario * 0.05
        percentual = '5%'
    novo_salario = reajuste + salario
    return novo_salario, reajuste, percentual


calculo = calculo_salario(salario)
mostar_mensagem(float(calculo[0]), float(calculo[1]), (calculo[2]))