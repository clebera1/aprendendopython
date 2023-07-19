numero = int(input('Informe um numero: '))

num1 = numero // 1 % 10
num2 = numero //10 % 10
num3 = numero // 100 % 10
num4 = numero // 1000 % 10

print(f'Unidade: {num1}')
print(f'Centena: {num2}')
print(f'Dezena: {num3}')
print(f'Milhar: {num4}')