

lista_adicionados = []
continuar = ''

while True:
    valores = int(input('Digite um valor: '))

    if valores in lista_adicionados:
        print('Numero já adicionado. Não irei adicionar novamente')
    else:
        print('Numero adicionado!')
        lista_adicionados.append(valores)
    continuar = str(input('Deseja continuar? '))

    if continuar.upper() == 'N':
        break
print('Os valores adicionados a lista foram: ', end = '')
print(sorted(lista_adicionados))