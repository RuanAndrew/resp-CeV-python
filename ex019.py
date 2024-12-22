from random import choice
n1 = input('digite o nome de um aluno: ')
n2 = input('digite o nome de mais um aluno: ')
n3 = input('digete o nome de mais u aluno: ')
n4 = input('digete o nome do ultimo aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'o aluno escolhido foi {escolhido}')
