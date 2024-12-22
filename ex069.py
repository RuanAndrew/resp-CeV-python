tot18 = homens = mulher20 = 0
while True:
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo: [M/F] ')).upper().strip()[0]
    if idade > 18:
        tot18 +=1
    if sexo == 'M':
        homens +=1
    if sexo == 'F' and idade < 20:
        mulher20 +=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('você quer continur: [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'total de pessoas com mais de 18 anos: {tot18}')
print(f'ao todo temos {homens} cadastrados')
print(f'e temos {mulher20} mulheres com menos de 20 anos')