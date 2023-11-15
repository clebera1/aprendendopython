from random import randint
from time import sleep
'''
numeros = []
lista = []
lista_total = []
print('=-' * 30 )
print('JOGO DA MEGA SENA')

jogos = int(input('Quantos jogos voce quer que eu sorteie? '))
print('=-' * 30)
print(f'Perfeito! Irei sortear {jogos} jogos para você. Boa sorte!!')

#Varias listas que no fim viram uma lista composta
for n in range(0,jogos):
    for c in range(1,7):
        numeros = randint(0,60)
        lista.append(numeros)
    lista.sort()
    print(f'Jogo {n+1}: {lista}')
    sleep(1)
    lista_total.append(lista[:])
    lista.clear()


#Lista composta
print(f'Perfeito! Irei sortear {jogos} jogos para você. Boa sorte!!')
for i, l in enumerate(lista_total):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
'''

#Sem repetir o numero de cada jogo da mega-sena (FAZER COMO PROXIMO EXERCICIO)

lista = []
numero = 0
contador = 0
lista_total = []
total = 1
jogos = int(input('Quantos jogos voce quer jogar? '))
while total <= jogos:
    contador = 0
    while True:
        numero = randint(0,60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
            
        if contador >= 6:
            break
    lista.sort()
    lista_total.append(lista[:])
    lista.clear()
    total += 1
    
for i, j in enumerate(lista_total):
    print(f'JOGO {i+1}: {j}')
    sleep(0.5)

print('Aqui estão os jogos que fiz para voce, boa sorte!')