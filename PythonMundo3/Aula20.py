def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos numeros {valores} é {s}.')

soma(1, 3, 4)
