total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('produto do produto: '))
    preco = float(input('preço: '))
    cont +=1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    continuar = str(input('voçe quer continuar [S/N]: ')).upper().strip()[0]
    if continuar in 'Nn':
        break
print(f'total: {total}')
print(f'tem {totmil} produtos que custam mais de 1000')
print(f'o produto mais barato foi {barato} que custa {menor}')