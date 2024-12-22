from math import sqrt
cateto_oposto = float(input('digete o valor do cateto oposto: '))
cateto_adjacente = float(input('digete o valor do cateto adjacente: '))
hipotenusa = sqrt((cateto_oposto ** 2 + cateto_adjacente ** 2))
print(f'o valor da hipotenusa e {hipotenusa:.2f}')
