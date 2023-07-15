s = str(input('Informe seu sexo [M/F]: ')).strip().upper() [0]
while s not in 'FfMm':
    s = str(input('Sexo incorreto, tente novamnete [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(s))
