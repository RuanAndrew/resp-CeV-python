import math
num = int(input('digite um numero: '))
fatorial = math.factorial(num)
while num >= 1:
    print(num,end='')
    print(' x ' if num > 1 else ' = ', end='')
    num -= 1
print(fatorial)
