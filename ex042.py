reta1 = float(input('digite o comprimento da primeira reta: '))
reta2 = float(input('digite o comprimento da segunda reta: '))
reta3 = float(input('digite o comprimento da terceira reta: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta3 + reta2 > reta1:
    print('essas retas podem formar um triangulo')
else:
    print('essas retas não podem formar um triangulo')
if reta1 and reta2 and reta3 == reta1:
    print('é um triangulo equilatero')
elif reta1 and reta2 == reta1 or reta1 and reta3 == reta1 or reta2 and reta3 == reta2:
    print('é um triangulo isósceles')
else:
    print('é um triangulo escaleno')