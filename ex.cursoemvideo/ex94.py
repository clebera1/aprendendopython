
lista_cadastros = []
continuar = 'Nn'
contador_pessoas = 0
soma_idade = 0
media_idade = 0
lista_idade = []
lista_idade_final = []
lista_acima_media = []
lista_mulheres = []
lista_acima_media_final = []

while continuar != 'N':

    cadastros = {}
    cadastros['nome'] = str(input('Nome: '))
    cadastros['sexo'] = str(input('Sexo: [M / F]').upper()[0])
    if cadastros['sexo'] == 'F':
            lista_mulheres.append(cadastros['nome'])
            lista_mulheres_final = lista_mulheres[:]

    
    if cadastros['sexo'] not in 'FfMm':
        cadastros['sexo'] = str(input('ERRO! O sexo precisa ser F ou M: ').upper()[0])
        if cadastros['sexo'] == 'F':
            lista_mulheres.append(cadastros['nome'])
            lista_mulheres_final = lista_mulheres[:]


    

    
    cadastros ['idade'] = int(input('Idade: '))

    lista_idade.append(cadastros['idade'])

    lista_idade_final = lista_idade[:]

    soma_idade += cadastros['idade']
    
    
    lista_cadastros.append(cadastros)
    del(cadastros)

    continuar = str(input('Deseja continuar? [S / N]').upper()[0])

    contador_pessoas = contador_pessoas + 1
    media_idade = soma_idade / contador_pessoas
    






    if continuar not in 'SsNn':
        continuar = str(input('ERRO! Voce precisa digitar S ou N: '))
        

for pessoas in lista_idade_final:
     if pessoas > media_idade:
          lista_acima_media.append(pessoas)



print('Cadastros finalizados!')

print(f'A) Foram cadastradas {contador_pessoas} pessoas')

print(f'B) media das idades é de {media_idade}')

if len(lista_mulheres) == 0:
    print('C) Nenhuma mulher foi cadastrada')
else:
     print(f'C) As mulheres cadastradas foram {lista_mulheres_final}')

print(f'D) As idades acima da media foram: {lista_acima_media}')

print('<<PROGRAMA ENCERRADO>>')