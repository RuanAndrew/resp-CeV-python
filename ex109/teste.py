import moeda

p = float(input('digite o preço: R$'))
print(f'a metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'o dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}')
print(f'aumentano 10%, temos {moeda.aumentar(p, 10,True)}')
print(f'reduzindo 13%, temos {moeda.diminuir(p, 13,True)}')