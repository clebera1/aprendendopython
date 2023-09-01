contador_idade = 0

homem_mais_velho = ''
maior_idade = 0
contador_mulheres = 0


for pessoas in range (1,5):
    print(f'Digite a {pessoas}a pessoa: ')
    nome = str(input('Seu nome: '))
    idade = int(input('Sua idade: '))
    sexo = str(input('Seu sexo [F/M]')).upper()

    if sexo != "M" or sexo != "F":
        print('Informação invalida')
    
    contador_idade = contador_idade + idade
    if pessoas == 1 and sexo == 'M':
        homem_mais_velho = nome
        maior_idade = idade

    if idade > maior_idade and sexo == 'M':
        homem_mais_velho = nome
        maior_idade = idade

    if sexo == 'F' and idade < 20:
        contador_mulheres = contador_mulheres + 1




        

media = contador_idade / 4

print(f'A media de idade desse grupo é de{media}')
print(f'O nome do homem mais velho é {homem_mais_velho}')
print(f'A quantidade de mulheres com menos de 20 anos é de {contador_mulheres}')