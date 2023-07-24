import random

print('Vou pensar em um numero entre 0 e 5. Tente adivinhar')
numero = int(input('qual numero acha que eu pensei? '))
random.randrange(0,5)
print('-=-' * 12)
print('processando....')
print('-=-' * 12)
print(f'O numero que escolhi foi {random.randrange(0,5)}')

if numero == random.randint:
    print('Parabens. Voce acertou!')
else:
    print('Voce errou')