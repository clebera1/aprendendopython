from time import sleep

#EX 115A - funcoes antes de entender resolução do exercicio


def criarMenu(msg):
    print('-' * 36)
    print(msg.center(36))
    print('-' * 36)

def opções():
    print('1 - Ver pessoas Cadastradas')
    print('2 - Cadastrar Nova Pessoa')
    print('3 - Sair do Sistema')

def inputUsuário(msg):
    try:
        sua_opcao = int(input(msg))
    except ValueError:
        sleep(0.8)
        print('ERRO! Digite um numero inteiro válido:')
    else:
        if sua_opcao == 1:
            sleep(0.8)
            criarMenu('OPÇÃO 1')
        elif sua_opcao == 2:
            sleep(0.8)
            criarMenu('OPÇÃO 2')
        elif sua_opcao == 3:
            sleep(0.8)
            criarMenu('Saindo do Sistema... Até logo!')  
        else:
            print('ERRO! Digite uma opção válida')    



