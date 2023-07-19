nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome em letras minusculas é: {nome.lower()}')
print(f'Seu nome em letras maisculas é: {nome.upper()}')
print(f'Seu nome ao todo tem {len(nome) - nome.count(" ")} letras')
'''print(f'Seu primeiro nome tem {nome.find(" ")} letras')'''
separar = nome.split()
print(f'Seu primeiro nome é {separar[0]} e tem {len(separar[0])} letras')
