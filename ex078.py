lista = []
maior = 0
menor = 0
for c in range(0,5):
    lista.append(int(input(f'digitte o calor a ser adicionado a posição {c}: ')))
    if c == 0:
        maior = lista[c]
        menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'você digitou {lista}')
print(f'o maior valor digitado foi {maior} nas posições ',end='')
for i,v in enumerate(lista):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'o menoror calor foi {menor}nas posições ',end='')
for i,v in enumerate(lista):
    if v == menor:
        print(f'{i}...',end='')
print()