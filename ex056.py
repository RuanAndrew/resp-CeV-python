soma_idade = 0
media_idade = 0
maioridade_homen = 0
nomevelho = ''
totalmulher20 = 0
for c in range(1,5):
    nome = input('seu nome: ')
    idade = int(input('sua idade: '))
    sexo = input('[M|F]: ').upper()
    soma_idade += idade
    if c == 1 and sexo == 'M':
        maioridade_homen = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridade_homen:
        maioridade_homen = idade
        nomevelho = nome
    if idade < 20 and sexo == 'F':
        totalmulher20 +=1
media_idade = soma_idade / 4
print(f'a media da idade de todos é {media_idade}')
print(f'o homen mais velho tem {maioridade_homen} anos e se chama {nomevelho}')
print(f'o total de mulheres com menos de 20 anos é {totalmulher20}')