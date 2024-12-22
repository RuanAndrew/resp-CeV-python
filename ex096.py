def area(larg,comp):
    a = larg*comp
    print(f'A area de um terreno {larg}x{comp} e de {a:.1f}m².')

print('controle de terrenos')
print('-'*20)
l = float(input('largura (m): '))
c = float(input('comprimento (m): '))
area(l,c)