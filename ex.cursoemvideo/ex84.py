lista_temp = []
lista = []
maior = menor = 0
while True:
    lista_temp.append(str(input('Nome: ')))
    lista_temp.append(float(input('Peso: ')))
    
    if len(lista) == 0:
        maior = menor = lista_temp[1]
    else:
        if lista_temp[1] > maior:
            maior = lista_temp[1]
        if lista_temp[1] < menor:
            menor = lista_temp[1]
    lista.append(lista_temp[:])
    lista_temp.clear()
    resp = str(input('Deseja continuar (S/N)').upper())
    if resp in 'Nn':
        break

print(f'Foram cadastrados {len(lista)} pessoas')
print(f'O maior peso foi de {maior}kgs e o menor peso foi de {menor}kgs ')
for p in lista:
    if p[1] == maior:
        print(f'A pessoa com o maior peso é o {p[0]}')
for p in lista:
    if p[1] == menor:
        print(f'A pessoa com o menor peso é o {p[0]}')