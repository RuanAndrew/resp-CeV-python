valor = int(input('qual o valor a ser sacado: '))
cinquenta = vinte = dez = um = 0
while True:
    if valor % 50 == 0:
        cinquenta += 1
        valor -= 50
        
    elif valor % 20 == 0:
        vinte += 1
        valor -= 20
        
    elif valor % 10 == 0:
        dez += 1
        valor -= 10
        
    elif valor % 1 == 0:
        um += 1
        valor -= 1
        
    if valor == 0:
        break
print(f'total de {cinquenta} cedulas de R$ 50')
print(f'total de {vinte} cedulas de R$ 20')
print(f'total de {dez} cedulas de R$ 10')
print(f'total de {um} cedulas de R$ 1')
print(f'volte sempre ao banco CEV! Tenha um bom dia!')