sexo = (input('qual o seu sexo? M ou F: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('dados invalidos. por favor, informe seu sexo[M/F]: ')).strip().upper()[0]
print(f'sexo {sexo} registrado com sucesso')
