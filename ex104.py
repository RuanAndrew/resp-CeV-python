def LeiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return n
        else:
            print('ERRO! Digite um numero inteiro valido.')


n = LeiaInt('digite um numero: ')
print(f'voce acabou de digitar o numero {n}')