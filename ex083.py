lista = []
aberto = 0
expresao = str(input('digite a expresão: '))
for n in expresao:
    if n in '()':
        lista.append(n)
for c in lista:
    if c in '(':
        aberto +=1
if aberto * 2 == len(lista):
    print('expresão valida')
else:
    print('expresão invalida')