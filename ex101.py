def voto(nascimeto):
    from datetime import datetime
    idade = datetime.now().year - nascimeto
    if 16 <= idade < 18 or idade > 65:
        situacao = 'VOTO OPCIONAL'
    elif idade >= 18:
        situacao = 'VOTO OBRIGATORIO'
    elif idade < 18:
        situacao = 'NÃO VOTA'
    return print(f'com {idade} anos: {situacao}')


usuario = int(input('ano de nascimento: '))
voto(usuario)