produto = float(input('qual o valor do produto?: '))
pagamento = int(input('qual a forma de pagamento?\n1 para dinheiro/cheque\n2 para a vista no cartão\n3 para em ate 2x no cartão\n4 para em 3x ou mais no cartão\n'))
if pagamento == 1:
    print(f'a vista/cheque o valor é {produto - (produto * 10/100)}')
elif pagamento == 2:
    print(f'a vista no cartão é {produto - (produto * 5/100)}')
elif pagamento == 3:
    print(f'em ate 2x no cartão é {produto}')
elif pagamento == 4:
    print(f'em ate 3x no cartão é {produto * 1.20}')
else:
    print('digite um valor valido')
