cont = 0
resultado = 0
from random import randint
while True:
    opcao = ' '
    while opcao not in (1,2):
        opcao = int(input('PAR(1) ou IMPAR(2)'))
    computador = randint(1,10)
    jogador = int(input('digite um numero de 1 a 10: '))

    soma = computador + jogador
    if opcao == 1:
        if soma % 2 == 0:
            print('você venceu')
            cont +=1
        else:
            print('você perdeu')
            break
    elif opcao == 2:
        if soma % 2 == 1:
            print('você venceu')
            cont +=1
        else:
            print('você perdeu')
            break
    print('vmos jogar novamente')
print(f'você jogou {jogador} e o computador {computador}. o total de {soma} DEU {resultado}')
print(f'você ganhou {cont} vezes seguidas')