soma = 0
for c in range(0,6):
    n = int(input(f'digite o {c+1}°inteiro: '))
    if n % 2 == 0:
        soma += n
print(f'a soma dos numeros pares é {soma}')
