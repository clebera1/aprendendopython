maior_peso = 0
menor_peso = 0

for pessoas in range(1,6):
    peso= float(input(f'Digite o peso da {pessoas}a pessoa: '))

    if pessoas == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f'O maior peso foi de {maior_peso} Kg')
print(f'O menor peso foi de {menor_peso} Kg')