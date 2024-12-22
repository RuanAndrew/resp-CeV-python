contagem = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
num = int(input('numero entre 0 e 10: '))
while num <0 or num > 10:
    num = int(input('numero entre 0 e 10: '))
print(contagem[num])
