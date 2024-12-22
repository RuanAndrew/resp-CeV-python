termo1 = int(input('digite o primeiro termo: '))
r = int(input('digite a razão: '))
decimo = termo1 + (10 - 1) * r
for c in range(termo1,decimo+1, r):
    print(c, end=" ")
