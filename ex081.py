lista = []
while True:
    print('-'*30)
    num = int(input('digite os valores da lista: '))
    print('-'*30)
    lista.append(num)
    resp = str(input('você quer continuar [S/N]: ')).upper().strip()[0]
    if resp not in 'SsNn':
        while resp not in 'SsNn':
            resp = str(input('você quer continuar [S/N]: ')).upper().strip()[0]
    if resp in 'Nn':
        break
print(f'você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('o numero 5 faz parte da lista')
else:
    print('o numero 5 não faz parte da lista')