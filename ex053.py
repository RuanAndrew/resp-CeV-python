frase = str(input('digite uma frase e eu direi se ela é um palíndromo ou não: ')).upper()
frase_nova = frase.replace(" ", "")
invertida = frase_nova[::-1]
print(f'o inverso de {frase_nova} é {invertida}')
if frase_nova == invertida:
    print('essa frase é um palindromo')
else:
    print('não é um paçindromo')
