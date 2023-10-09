n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
n4 = int(input('Por fim, digite o ultimo numero: '))
numeros = n1, n2, n3, n4
print(f'Voce digitou os valores: {numeros}')
print(f'O numero 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O primeiro valor 3 que foi digitado apareceu na posição {numeros.index(3)+1}')
else:
    print('Nesse caso o valor 3 nao apareceu')
print(f'Os valores digitados que são pares são: ', end = '')
for n in numeros:
    if n % 2 == 0:
        print(n, end = ' ')
