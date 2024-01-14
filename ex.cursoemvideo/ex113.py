def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('Digite um numero inteiro valido:')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return valor



def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print(f'Digite um numero real valido.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return valor
        

inteiro = leiaInt('Digite um numero inteiro:')
real = leiaFloat('Digite um numero real:')
print(f'O numero inteiro que voce digitou foi o {inteiro} e o real foi {real}')