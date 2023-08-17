'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''



def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if (idade < 16):
        return f'Com sua idade de {idade} anos, o voto é: não necessario!'
    elif (16 <= idade < 18) or (idade >= 70):
        return f'Com sua idade de {idade} anos,o voto é: opcional!'
    else:
        return f'Com sua idade de {idade} anos, o voto é: obrigatorio!'



nasc= int(input('Qual seu ano de nascimento: '))
print(voto(nasc))