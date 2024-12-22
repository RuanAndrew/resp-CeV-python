num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))
programa = (1,2,3,4,5)
while programa != 5:
    programa = int(input('''menu
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
'''))
    if programa == 1:
        print(f'a soma entre {num1} e {num2} é {num1 + num2}')
    elif programa == 2:
        print(f'a multiplicação entre {num1} e {num2} é {num1 * num2}')
    elif programa == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        elif num1 == num2:
            print(f'{num1} é {num2} tem o mesmo valor')
        else:
            print(f'{num2} é maior que {num1}')
    elif programa == 4:
        num1 = int(input('digite o novo primeiro numero: '))
        num2 = int(input('digite o novo segundo numero: '))
    elif programa > 5 or programa < 1:
        print('opção invalida')
print('programa encerrado')