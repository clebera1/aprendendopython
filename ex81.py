lista = []
cont = 0
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    cont +=1
    c = str(input('Deseja continuar? S/N ')).upper()
    if c == 'N':
        break

print(f'Foram digitados {len(lista)} numeros')
lista.sort(reverse=True)
print(f'Essa lista em ordem decrescente é: {lista}')
if 5 in lista:
    print('O numero 5 faz parte da lista')
else:
    print('O numero 5 nao faz parte da lista')