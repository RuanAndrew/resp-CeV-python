matriz = [[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'digite um valor para a [{l},{c}]: ')))
soma_par = soma_coluna3 = maior_2l = 0
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()