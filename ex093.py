jogador = {}
jogador['nome'] = str(input('Nome: '))
tot = int(input('Quantidade de partidas: '))
partidas = []
soma = 0
for c in range(0,tot):
    partidas.append(int(input(f'quantos gols na {c+1}° partida: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'{k} tem valor {v}')
print('=-' * 30)
print(f'o jogador {jogador["nome"]} jogol {len(jogador["gols"])}')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i+1} fez {v} gols.')
print(f'um total de {jogador["total"]} gols')
