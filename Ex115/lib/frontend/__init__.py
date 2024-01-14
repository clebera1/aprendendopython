from time import sleep

def linha(tam = 42):
    return '-' * tam


def leiaInt(numero):
    while True:
        try:
            valor = int(input(numero))
        except (ValueError, TypeError):
            print('ERRO! Insira um valor válido. ')
        else:
            return valor


def cabeçalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())



def menu(lista):
    cabeçalho('MENU DE OPÇÕES')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opcao = leiaInt('Sua opção: ')
    return opcao
