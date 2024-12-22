num1 = int(input('digite um numero: '))
num2 = int(input('digite outro: '))
if num1 > num2:
    print(f'o numero {num1} é maior que {num2}')
elif num2 > num1:
    print(f'o numero {num2} é maior que {num1}')
else:
    print(f'os numeros {num1} e {num2} tem valores iguais')
