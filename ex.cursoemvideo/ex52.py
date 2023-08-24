numero = int(input('Digite um numero: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end = '')
        total = total + 1
    else:
        print('\033[31m', end = '')
    print(f'{c}', end = ' ')
print(f'\n\033[mO numero {numero} foi divisisel {total} vezes')
if total == 2:
    print(f'O numero {numero} é primo')
else:
    print(f'O numero {numero} não é primo')