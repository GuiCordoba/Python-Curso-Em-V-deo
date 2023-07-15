from datetime import date
atual = date.today().year
sexo = str(input('Seu sexo [F/M]:'))

if sexo == 'M':
    anonasc = int(input('Ano de nascimento: '))
    idade = atual - anonasc
    if idade < 18:
        tempof = 18 - idade
        print("Idade: {} anos".format(idade))
        print('Você ainda não tem idade para se alistar. Faltam {} anos.'. format(tempof))
    elif idade >= 18 and idade <= 50:
        tempof = idade - 18
        print("Idade: {} anos".format(idade))
        print('Você já pode se alistar. Já passaram {} anos para o alistamento!'.format(tempof))
    else:
        print("Idade: {} anos".format(idade))
        print('Não precisa se alistar, idade além da permitida!')
else:
    print('Você não precisa se alistasr!')