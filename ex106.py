def ajuda(com):
    titulo(f'acessando o manual do {com}')
    help(com)


def titulo(msg):
    tam = len(msg) + 4
    print('~'* tam)
    print(f'  {msg}')
    print('~'* tam)


comando = ''
while True:
    titulo('sistema de ajuda PyHELP')
    comando = str(input("funçao ou blibioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO')