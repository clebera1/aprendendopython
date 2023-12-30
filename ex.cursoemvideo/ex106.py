def manual(comando):
    print(help(com))

def titulo(msg, cor = 0):
    tamanho = len(msg)
    print('=' * tamanho)
    print(msg)
    print('=' * tamanho)


while True:
    titulo('PEÇA AJUDA AO SISTEMA')
    com = str(input('Função ou biblioteca > '))
    if com.upper() == 'FIM':
        break
    else:
        manual(com)
titulo('Programa Finalizado!')