matriz = [[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'digite um valor para a [{l},{c}]: ')))
soma_par = soma_coluna3 = maior_2l = 0
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
        #soma dos pares
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        #soma da terceira coluna
        if c == 2:
            soma_coluna3 += matriz[l][c]
        #maior valor segunda linha
        if l == 1:
            if l == 0:
                maior_2l = matriz[l][c]
            else:
                if matriz[l][c] > maior_2l:
                    maior_2l = matriz[l][c]
    print()
        
print(f'a soma dos valores pares é {soma_par}')
print(f'a soma dos valores da terceira coluna é {soma_coluna3}')
print(f'o maior valor da segunda linha é {maior_2l}')