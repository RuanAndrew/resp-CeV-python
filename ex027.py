n = str(input('digite seu nome completo: ')).strip()
nome = n.split()
print(f'seu primeiro nome é {nome[0]}')
print(f'seu ultimo nome é {nome[len(nome)-1]}')
