def leiaInt(msg):
    while True:
        try:
            entrada = int(input(msg))
            if entrada < 1 or entrada > 3:
                print('ERRO: Digite uma opção válida!')
                continue
        except(ValueError,TypeError):
            print('ERRO: por favor, digite um numero inteiro valido')
        except (KeyboardInterrupt):
            print('entrada de dados interrompida pelo usuario')
            return 3
        else:
            return entrada


def linha(tam=40):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())
    

def menu():
    from time import sleep
    import arquivo
    while True:
        cabecalho('MENU PRINCIPAL')
        print('1 - Ver pessoas cadastradas')
        print('2 - Cadastrar nova pessoa')
        print('3 - Sair do sistema')
        print(linha())

        opcao = leiaInt('Sua opção: ')
        arq = 'cursoemvideo.txt'

        if not arquivo.arquivoExiste(arq):
            arquivo.criarArquivo(arq)

        if opcao == 1:
            arquivo.lerArquivo(arq)
            sleep(1)
        elif opcao == 2:
            cabecalho('NOVO CADASTRO')
            nome = str(input('nome: '))
            idade = int(input('idade: '))
            arquivo.cadastrar(arq,nome,idade)
            sleep(1)
        elif opcao == 3:
            cabecalho('Saindo do sistema... Até logo!')
            sleep(1)
            break