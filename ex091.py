from random import randint
from operator import itemgetter
jogo = {}
for c in range(1,5):
    jogo[f'jogador{c}'] = randint(1,6)
ranking = ()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print(' == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')