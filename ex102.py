def fatorial(n,show=False):
    """
    -> calcula o fatorial de um numero
    :param n: O numero a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: O valor do fatorial do numero n."""
    print('-'*30)
    soma = 1
    for c in range(n,0,-1):
        if show == True:
            print(c,end='')
            if c > 1:
                print(' X ',end='')
            else:
                print(' = ',end='')
        soma *= c
    return soma
print(fatorial(5,show=True))