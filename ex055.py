maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('qual é o seu peso: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'a pessoa com maior peso tem {maior}KG\na pessoa com menor peso tem {menor}KG')
