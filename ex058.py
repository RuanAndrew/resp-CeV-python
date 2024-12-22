from random import randint
cont = 0
num = randint(0,10)
tentativa = int(input('tente adivinhar o numero que eu pensei entre 0 e 10: '))
while tentativa != num:
    print(f'eu pensei em {num} você escolheu {tentativa}. Você errou')
    num = randint(0,10)
    tentativa = int(input('tente novamente: '))
    cont += 1
if tentativa == num:
    print(f'eu pensei em {num} você escolheu {tentativa}. parabens voce acertou em {cont+1} tentativas')
