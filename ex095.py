grupo = []
jogador = {}
while True:
    jogador['nome'] = str(input('Nome: '))
    tot = int(input('Quantidade de partidas: '))
    partidas = []
    soma = 0
    for c in range(0,tot):
        partidas.append(int(input(f'quantos gols na {c+1}° partida: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    grupo.append(jogador.copy())
    resp = str(input('quer continuar [S/N]: '))
    while resp not in 'SsNn':
        resp = str(input('quer continuar [S/N]: '))
    if resp in 'Nn':
        break
print('-'* 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'* 40)
for k, v in enumerate(grupo):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'* 40)
while True:
    busca = int(input('mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(grupo):
        print(f'ERRO! Não existe jogador com codigo {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {grupo[busca]["nome"]}: ')
        for i, g in enumerate(grupo[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-'*40)
print('<<VOLTE SEMPRE>>')