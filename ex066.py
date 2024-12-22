soma = cont = 0
while True:
    n = int(input('digite os numeros(999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'foram digitados {cont} numeros, a soma deles é {soma}.')