import datetime
nascimento = int(input('digite o ano do seu nascimento: '))
data = datetime.date.today().year
idade = data - nascimento
if idade <= 9:
    print('sua categoria é: MIRIM')
elif idade <= 14:
    print('sua categoria é: INFANTIL')
elif idade <= 19:
    print('sua categoria é: JUNIOR')
elif idade <= 25:
    print('sua categoria é: SÊNIOR')
else:
    print('sua categoria é: MASTER')
