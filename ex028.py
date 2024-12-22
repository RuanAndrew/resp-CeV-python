from random import randint
num = randint(0,5)
tentativa = int(input('tente adivinhar o numero que eu pensei entre 0 e 5: '))
if tentativa == num:
    print('parabens voce acertou')
else:
    print('voce errou')
