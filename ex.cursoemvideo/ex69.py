maior = mulher = homem = 0
while True:
    idade = (int(input('Qual sua idade? ')))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo?')[0]).upper()
        if idade > 18:
            maior += 1
        if sexo == 'M':
            homem += 1
        if idade < 20 and sexo == 'F':
            mulher += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).upper()
    if continuar == 'N':
        break

print(f'{homem} homens foram cadastrados')
print(f'{maior} pessoas com mais de 18 anos foram cadastradas')
print(f'{mulher} mulheres com menos de 20 anos foram cadastradas')