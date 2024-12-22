import moeda

p = float(input('digite o preço: R$'))
print(f'a metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'o dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'aumentano 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')