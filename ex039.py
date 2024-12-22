import datetime
nascimento = int(input('digite o ano do seu nascimento: '))
data = datetime.date.today().year
if data - nascimento < 18:
    print(f'ainda não é hora de se alistar. faltam {18 - (data - nascimento)} anos')
elif data - nascimento == 18:
    print(f'é hora de se alistar.')
else:
    print(f'já passou do tempo do alistamento. passou {abs(18 - (data - nascimento))} anos')
