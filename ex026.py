nome = str(input('digite seu nome completo: ')).strip().upper()
print(f'a letra A apareçe {nome.count("A")} vezes')
print(f'a letra A apareçe na posição {nome.find("A")+1}')
print(f'a ultima letra a apareçe na posoção {nome.rfind("A")+1 }')