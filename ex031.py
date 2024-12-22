distancia = int(input('qual a distancia da viagem?: '))
if distancia <= 200:
    print(f'sua viagem vai custar {distancia * 0.5}')
else:
    print(f'sua viagem vai custar {distancia * 0.45}')
