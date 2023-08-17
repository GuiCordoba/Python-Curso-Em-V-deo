'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas  – A maior nota– A menor nota – A média da turma- A situação (opcional)'''

def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de varios alunos
    :param n: uma ou mais notas do aluno (aceita mais de umna)
    :param sit: valor adicional, indica se deve ou não adicionar a situação
    :return: retorna um dicionario com varias informações do aluno
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['memor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA!'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL!'
        else:
            r['situacao'] = 'RUIM'
    return r



#Programa Principal
resp = notas(9, 7, 5, sit=True)
print(resp)
help(notas)