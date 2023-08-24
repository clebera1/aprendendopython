contador_idade = 0
maior_idade = 0
nome_mais_velho = ''
contador_sexo = 0


for pessoas in range(1,3):
    print(f'==== {pessoas}A PESSOA ====')
    nome = str(input('Seu nome: '))
    idade = float(input('Idade: '))
    contador_idade = contador_idade + idade
    sexo = str(input('Sexo [M/F]: ')).upper()

    if pessoas == 1 and sexo == 'M':
        maior_idade = idade
        nome_mais_velho = nome
    if sexo == 'M' and idade > maior_idade:
        nome_mais_velho = nome
        maior_idade = idade
    if sexo == 'F' and idade < 20:
        contador_sexo = contador_sexo + 1

        
media = contador_idade / 4


'''        contador_sexo = [sexo]
    else:
        contador_sexo.append(sexo)
    if sexo == 'M':
        if pessoas == 1:
            maior_idade = idade
        else:
            if idade > maior_idade:
                idade = maior_idade     '''

print(f'A media de idade desse grupo é de {media}')
print(f'O nome do homem mais velho é {nome_mais_velho}')
print(f'E há {contador_sexo} mulheres abaixo de 20 anos')






#print(f'O nome dos homens são {contador_nome}')



#media = contador_idade / 4


#print(f'A media de idade desse grupo é de {media}')