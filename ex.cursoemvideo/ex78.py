'''lista = []
for posicao in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {posicao + 1}:')))

print(f'O maior valor dessa lista é o {max(lista)} e o menor é o {min(lista)}')
print(posicao)'''

lista = []
maior = menor = 0
for posicao in range(0,5):
    lista.append(int(input(f'Digite um valor para a posicao {posicao + 1}: ')))
    if posicao == 0:
        maior = menor = lista[posicao]
    else:
        if lista[posicao] > maior:
            maior = lista[posicao]
        if lista[posicao] < menor:
            menor = lista[posicao]
print(f'Voce digitou os valores {lista}')
print(f'O maior valor é o {maior} nas posicoes ', end = '')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i+1}...', end='')
print()
print(f'e o menor é o {menor} nas posicoes ', end = '')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i+1}...', end = '') 
