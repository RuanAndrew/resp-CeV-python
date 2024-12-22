import datetime
ano = datetime.date.today().year
soma1 = 0
soma2 = 0
for c in range(1,8):
    idade = int(input('qual o ano do seu nascimento: '))
    if ano - idade < 21:
        print(f'você é menor de idade')
        soma1  += 1
    else:
        print(f'você é maior de idade')
        soma2 +=1
print(f'{soma1} pessoas são menores de idade')
print(f'{soma2} pessoas são maiores de idade')
