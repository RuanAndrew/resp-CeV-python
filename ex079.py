lista = []
while True:
    print('-'*30)
    num = int(input('digite os valores da lista: '))
    print('-'*30)
    if num not in lista:
        lista.append(num)
    else:
        print('valor duplicado! Não vou adicionar')
    resp = str(input('você quer continuar [S/N]: ')).upper().strip()[0]
    if resp not in 'SsNn':
        while resp not in 'SsNn':
            resp = str(input('você quer continuar [S/N]: ')).upper().strip()[0]
    if resp in 'Nn':
        break
print(sorted(lista))