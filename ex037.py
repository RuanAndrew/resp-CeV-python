num = int(input('escreva um numero inteiro: '))
base = int(input('digite uma base de conversão.\n1 para binario \n2 para octal \n3 para hexadecimal\n'))
if base == 1:
    print(f'o numero {num} em binario é {bin(num)[2:]}')
elif base == 2:
    print(f'o numero {num} em octal é {oct(num)[2:]}')
elif base == 3:
    print(f'o numero {num} em hexadecimal é {hex(num).upper()[2:]}')
else:
    print('digite um valor valido')
