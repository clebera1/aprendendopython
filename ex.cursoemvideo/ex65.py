'''contador = 0
continuar = ''
soma = 0
menor = 9999
maior = 1
numero = 1
while continuar != 'N':
    numero = int(input('Digite um numero: '))
    soma = soma + numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    continuar = str(input('Quer continuar? [S/N]')[0].upper())
    contador = contador + 1
media = soma / contador
print(f'A media entre todos esses valores é: {media}') 
print(f'O maior numero é o {maior}')
print(f'O menor numero é o {menor}')
'''

resposta = 'S'
contador = soma = maior = menor = 0
while resposta in 'Ss':
    numero = int(input('Digite um numero: '))
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Deseja continuar?[S/N]').upper().strip()[0])

media = soma / contador 
print(f'Voce digitou {contador} valores e a media deles foi: {media}')
print(f'O maior valor é o {maior} e o menor valor é o {menor}')
