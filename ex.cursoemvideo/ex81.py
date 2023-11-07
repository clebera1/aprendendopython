numeros = 0
lista = []
pares = []
impares = []
while True:
    numeros = (int(input('Digite um numero: ')))
    lista.append(numeros)
    if numeros % 2 ==0:
        pares.append(numeros)
    else:
        impares.append(numeros)
    resp = str(input('Deseja continuar? S/N ')).upper()
    if resp == 'N':
        break
lista.sort()
print(f'Sua lista em ordem crescente está assim: {lista}')
print(f'Os valores pares da sua lista são: {pares}')
print(f'Os valores impares da sua lista são: {impares}')
