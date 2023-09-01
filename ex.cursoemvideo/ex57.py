sexo = str(input('Informe seu sexo:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Valor invalido. Digite novamente')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')