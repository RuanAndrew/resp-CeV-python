num = int(input('digite o primeiro termo: '))
r = int(input('digite a razão: '))
PA = 0
quant_termo = 10
cont = 1
while PA <= quant_termo:
    print(num,end=" ")
    PA += 1
    num += r
    cont +=1
    if PA == quant_termo:
        quant_termo = int(input('quantos termos a mais você quer mostrar?: '))
        PA = 0
        if quant_termo ==  0:
            print(f'programa encerrado com {cont} termos')
    continue
