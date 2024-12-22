num = int(input('digite um numero inteiro: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        total += 1
print(f'o numero {num} foi divisivel {total} vezes')
if total == 2:
    print('e por isso ele é primo')
else:
    print('e por isso ele nâo e primo')
