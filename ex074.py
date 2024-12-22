from random import randint
tupla = ()
for c in range(0,5):
    num = randint(1,10)
    tupla
    if c == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    print(num,end=' ')
print(f'\no maior é {maior}')
print(f'o menor é {menor}')