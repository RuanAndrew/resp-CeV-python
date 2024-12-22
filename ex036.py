valor_casa = int(input('qual o valor da casa?: '))
salario = int(input('qual o seu salario?: '))
anos = int(input('vai ser parcelada em quantos anos?: '))
parcelas = valor_casa / (anos * 12)
if parcelas >= (30/100 * salario):
    print(f'sua compra foi negada pois as parcelas de {parcelas:.2f} são maiores que 30% do seu salario')
else:
    print(f'sua compra foi aceita as parcelas serão de {parcelas:.2f}')
