dias = int(input('por quantos dias o carro foi aluguado? '))
km = float(input('por quantos kilometros o carro percorreu? '))
preco = km * 0.15 + dias * 60
print(f'o preço total a ser pago e de {preco:.2f}')
