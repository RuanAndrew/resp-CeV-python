def aumentar(preco=0, taxa=0,formato=False):
    res = moeda(preco + (preco * taxa/100))
    return res if formato is False else moeda(res)

def reduzir(preco=0, taxa=0,formato=False):
    res = moeda(preco - (preco * taxa/100))
    return res if formato is False else moeda(res)


def dobro (preco=0,formato=False):
    res = moeda(preco * 2)
    return res if formato is False else moeda(res)


def metade (preco=0,formato=False):
    res = moeda(preco / 2)
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco=0,aumneto=10,reducao=5):
    print('-'* 35)
    print('RESUMO DO VALOR'.center(35))
    print('-'* 35)
    print(f'preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco,True)}')
    print(f'Metade do preço: \t{metade(preco,True)}')
    print(f'{aumneto}% de aumento: \t{aumentar(preco,aumneto,True)}')
    print(f'{reducao}% de aumento: \t\t{reduzir(preco,reducao,True)}')
    print('-'*35)