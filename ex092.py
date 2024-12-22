from datetime import datetime
dados = {}
dados['nome'] = str(input('nome: '))
nascimento = int(input('ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('ano de contratação: '))
    dados['salario'] = float(input('salario: '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - datetime.now().year
print('-=' * 30)
print(' == DADOS ==')
for k, v in dados.items():
    print(f'{k}: {v}')