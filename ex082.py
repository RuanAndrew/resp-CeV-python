lista = []
lista_par = []
lista_impar = []
while True:
    print('-'*30)
    num = int(input('digite os valores da lista: '))
    print('-'*30)
    lista.append(num)
    # if num % 2 == 0:
        # lista_par.append(num)
    # else:
        # lista_impar.append(num)
    resp = str(input('você quer continuar [S/N]: ')).upper().strip()[0]
    if resp not in 'SsNn':
        while resp not in 'SsNn':
            resp = str(input('você quer continuar [S/N]: ')).upper().strip()[0]
    if resp in 'Nn':
        break
for n in lista:
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
print(lista)
print(lista_par)
print(lista_impar)