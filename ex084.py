pessoa = []
galera = []
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    galera.append(pessoa[:])
    pessoa.clear
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print(f'Ao todo, você cadastrou {len(galera)} pessoas')
print(f'o Maior peso foi de {maior}KG. peso de ',end='')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}]',end='')
print()
print(f'O menor peso foi de {menor}KG. peso de ',end='')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]}',end='')
print()