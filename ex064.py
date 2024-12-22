soma = 0
cont = 0
n = 0
while n != 999:
    n = int(input('digite um numero, caso deseje parar digite 999: '))
    if n != 999:
        soma += n
        cont += 1
print(f'foram digitados {cont} numeros, a soma entre eles é de {soma}')