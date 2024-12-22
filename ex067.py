tabulando =  1
while True:
    tabuada = int(input('quer ver a tabuada de qual valor: '))
    if tabuada < 0:
        break
    while tabulando <= 10:
        print(f'{tabuada} X {tabulando} = {tabuada*tabulando}')
        tabulando += 1
    tabulando = 1
print('PROGRAMA ENCERRADO')