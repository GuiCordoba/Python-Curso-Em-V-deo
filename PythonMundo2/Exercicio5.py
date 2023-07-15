def calcular_dias(n_funcionarios, n_maquinas, dias):
    return (n_funcionarios * n_maquinas * dias) / (20 * 150)

n_funcionarios = 30
n_maquinas = 275
dias = 45

dias_necessarios = calcular_dias(n_funcionarios, n_maquinas, dias)
print(f"Seriam necessários {dias_necessarios} dias para que os 30 funcionários preparassem as 275 máquinas.")
