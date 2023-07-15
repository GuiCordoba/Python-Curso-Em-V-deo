velo = int(input('Informe a velocidade do carro (km/h):'))
if velo > 80:
    multa = (velo - 80) * 7
    print('>>Velocidade acima do limite permitido. Voce foi multado!\n>>Valor da multa: R${}'.format(multa))
print('Velocidade dentro do permitido!')
