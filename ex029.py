velo = float(input('qual a velocidade do carro?: '))
if velo > 80:
    print(f'voce estava {velo - 80}km acima do limite da rua, isso é uma multa de {(velo - 80) * 7}')
else:
    print('voce estava dentro do limite da rua')
