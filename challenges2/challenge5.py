'''def lista_menor_1000(lista_numeros):
    nova_lista = []
    for numero in lista_numeros:
        if numero < 1000:
            nova_lista.append(numero)
    print(nova_lista)

lista_menor_1000([3, 2567, 5, 233,70550, 23, 30, 5000, 45])'''

def numeros_par(lista_numeros):
    nova_lista = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            nova_lista.append(numero)
    print(f'Os numeros pares dessa lista são: {nova_lista}')

numeros_par([12,3,4,5,5,6,7,87,3,2,254,6,7,5,3,2134,5,674,54,2,34,2,8898,6,6])
