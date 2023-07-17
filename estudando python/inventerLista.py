'''lista = [1,2,3,4,5,6,7,8,9,10]

lista_invertida = []

for numeros in range(len(lista)-1, -1, -1):
    lista_invertida.append(lista[numeros])
    
print(lista_invertida)'''

numeros = [1,2,3,4,5,6,7,8,9]
fim = len(numeros) - 1

for numero in range(len(numeros)):
    aux = numeros[numero]
    numeros[fim] = aux
    fim = fim - 1 