'''n = int(input('Digite um numero: '))
fatorial = n - 1

while fatorial != 1:
    n = n * fatorial
    fatorial = fatorial - 1


print(f'O fatorial do numero digitado é {n}')
    '''

n = int(input('Digite um numero: '))
c = n
fatorial = 1
print(f'Calculando o fatorial de {n}!')
while c > 0:
    print(c, end = "")
    print('x' if c > 1 else '=', end = '')
    fatorial = fatorial * c
    c = c - 1
print(fatorial)



'''n = int(input('Digite um numero: '))
c = n
f = 1
print(f'O fatorial de {n}! é:')
for c in range (n, 0, -1):
    print(c, end=' ')
    print('x ' if c > 1 else '=', end=' ')
    f = f * c
print(f)
'''