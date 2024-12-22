import random
itens = ('pedra', 'papel', 'tesoura')
jogador = int(input('vamos jogar jokenpô\n0 para pedra\n1 para papel\n2 para tesoura\n'))
computador = random.randint(0,2)
print(f'computador jogou {itens[computador]}')
print(f'você jogou {itens[jogador]}')
if jogador == 0 and computador == 2:
    print("você ganhou")
elif jogador == 1 and computador == 0:
    print("você ganhou")
elif jogador == 2 and computador == 1:
    print("você ganhou")
elif computador == 0 and jogador == 2:
    print('você perdeu')
elif computador == 1 and jogador == 0:
    print('você perdeu')
elif computador == 2 and jogador == 1:
    print('você perdeu')
else:
    print('empate')
