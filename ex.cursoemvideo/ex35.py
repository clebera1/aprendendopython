
print('-=-' * 20)
print('Analisador de Triangulos')
print('-=-' * 20)

a1 = float(input('Digite o valor do primeiro segmento:'))
a2 = float(input('Digite o valor do segundo segmento:'))
a3 = float(input('Digite o valor do terceiro segmento:'))


if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2:
    print(f'Esses segmentos podem formar um triangulo')
else:
    print('Esses segmentos nao podem formar um triangulo')