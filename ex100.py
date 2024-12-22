from random import randint
def sorteia(lista):
    print('sorteando 5 valores da lista: ',end='')
    for c in range(0,5):
        n = (randint(1,10))
        lista.append(n)
        print(n,end='')
    print()


def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'somando os valores pares de {lista} temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
