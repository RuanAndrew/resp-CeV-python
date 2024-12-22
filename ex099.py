def maior(*num):
    cont = maior = 0
    for v in num:
        print(f'{v}',end=' ')
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont +=1
    print(f'foram informados {cont} valores')
    print(f'o maior valor foi {maior}')

maior(2,9,4,5,7,1)
maior(4,7,8)
maior(6)
maior()