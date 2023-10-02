from random import randint
'''cont = maior = menor = 0
numeros = (randint(0,10)),(randint(0,10)),(randint(0,10)),(randint(0,10)),(randint(0,10))
print('Os valores sorteados foram: ', end = '')
for numero in numeros:
    if cont == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    cont += 1
    print(f'{numero}', end = ' ')
print(f'O maior valor dessa tupla é o {maior} e o menor é o {menor}')'''

numeros = (randint(0,10)),(randint(0,10)),(randint(0,10)),(randint(0,10)),(randint(0,10))

for numero in numeros:
    print(numero, end = ' ')
print(f'O maior valor dessa tupla é o {max(numeros)} e o menor é o {min(numeros)} ')






    