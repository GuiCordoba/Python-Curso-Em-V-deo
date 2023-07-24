'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times, b) Os últimos 4 colocados, c) Times em ordem alfabética, d) Em que posição está o time do Cruzeiro.'''
time = ("América-MG", "Athletico-PR", "Atlético-MG", "Bahia", "Botafogo", "Corinthians", "Coritiba", "Cruzeiro", \
"Cuiabá", "Flamengo", "Fluminense", "Fortaleza", "Goiás", "Grêmio", "Internacional", "Palmeiras", "Bragantino", "Santos", "São Paulo", "Vasco da Gama")

print('=' * 90)
print(f'Os 5 primeiros times são: {time[:5]}')
print('=' * 90)
print(f'Os ultimos 4 colocados são: {time[-4:]}')
print('=' * 90)
print(f'Os times em ordem alfabetica: {sorted(time)}')
print('=' * 90)
print(f'O time do cruzeiro esta na {time.index("Cruzeiro") + 1} posição.')
print('=' * 90)