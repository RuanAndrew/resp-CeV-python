def contador(i,f,p):
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    if i < f:
        print(f'contagem de {i} até {f} de {p} em {p}')
        for p in range(i,f+1,p):
            print(p,end=' ')
        print()
    else:
        print(f'contagem de {i} até {f} de {p} em {p}')
        while i >= f:
            print(i,end=' ')
            i -= p
        print()
    print('-='*30)

contador(1,10,1)
contador(10,0,2)
contador(
    i=int(input('Inicio: ')),
    f=int(input('fim: ')),
    p=int(input('passo: ')))
