import random

jogador = int(input("Selecione sua opção:\n[1] Pedra.\n[2] Papel.\n[3] Tisoura.\n-->>"))
seq = str("Pedra", "Papel", "Tesoura")
maquina = random.choice(seq)
print(maquina)