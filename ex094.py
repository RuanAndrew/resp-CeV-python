grupo = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while pessoa['sexo'] not in 'MmFf':
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())
    resp = str(input('quer continuar [S/N]: ')).upper().strip()[0]
    while resp not in 'SsNn':
        resp = str(input('quer continuar [S/N]: ')).upper().strip()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo foram cadastradas {len(grupo)} pessoas')
media = soma / len(grupo)
print(f'a media das idades é {media:5.2f} anos')
print(F'as mulheres cadastradas foram ',end='')
for p in grupo:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}',end=' ')
print()
print('lista de pessoas acima da media: ')
for p in grupo:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('programa encerrado')