numero = 0
contagem = 0
soma = 0
numero = int(input('Digite um numero: [999 p/ parar]'))
while numero != 999:
            soma = soma + numero
            contagem = contagem + 1
            numero = int(input('Digite um numero: [999 p/ parar]'))


print(f'Voce inseriu {contagem} valores e a soma deles foi um total de {soma}')
