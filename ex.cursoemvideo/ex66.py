soma = contador = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor == 999:
        break
    contador += 1
    soma += valor
    
print(f'Programa encerrado! Voce digitou {contador} valores e a soma deles é de: {soma}')