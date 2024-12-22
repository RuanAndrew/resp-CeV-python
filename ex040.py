nota1 = float(input('digite sua primeira nota: '))
nota2 = float(input('digite sua segunda nota: '))
media = (nota1 + nota2) /2
if media < 5:
    print('REPROVADO')
elif media < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
