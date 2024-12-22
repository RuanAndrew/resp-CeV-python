def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um numero inteiro valido')
            continue
        except (KeyboardInterrupt):
            print('entrada de dados interrompida pelo usuario')
            return 0
        else:
            return n
            

def LeiaFloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um numero inteiro valido')
            continue
        except (KeyboardInterrupt):
            print('entrada de dados interrompida pelo usuario')
            return 0
        else:
            return f
        
n = LeiaInt('digite um numero inteiro: ')
f = LeiaFloat('digite um numero real: ')
print(f'o numero inteiro digitado foi {n}')
print(f'o numero real digitado foi {f}')