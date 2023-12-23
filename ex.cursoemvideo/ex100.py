
from random import randint
from time import sleep

'''
Sem passar parametros

numeros = []
pares = []

print('Sorteando numeros...')
sleep(0.8)
def sorteia():
    for n in range(1,6):
        n = randint(0,10)
        numeros.append(n)
    print(f'Os numeros sorteados da lista foram: ', end = '')
    for n in numeros:
        print(n, end = ' ')
    print()

def somaPar():
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        soma_numeros_pares = sum(pares)
    print(f'A soma dos numeros pares dessa lista é igual a {soma_numeros_pares}')

sorteia()
somaPar()
'''

numeros = []
def sorteia(lista):
    for cont in range(1,6):
        n = randint(1,10)
        lista.append(n)
    print(f'Os numeros sorteados foram {lista} ')
def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma+=valor
    print(f'A soma dos numeros pares sorteados foi: {soma}')

sorteia(numeros)
somaPar(numeros)