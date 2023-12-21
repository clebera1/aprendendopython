
lista_cadastros = []
cadastros = {}
soma_idade = media_idade = 0

while True:
    cadastros['nome'] = str(input('Nome: '))
    cadastros['sexo'] = str(input('Sexo: [M / F]').upper()[0])

    if cadastros['sexo'] not in 'FfMm':
        cadastros['sexo'] = str(input('ERRO! O sexo precisa ser F ou M: ').upper()[0])

    cadastros ['idade'] = int(input('Idade: '))

    soma_idade += cadastros['idade']
    
    
    lista_cadastros.append(cadastros.copy())
    cadastros.clear()

    continuar = str(input('Deseja continuar? [S / N]').upper()[0])
    if continuar == 'N':
        break
    if continuar not in 'SsNn':
        continuar = str(input('ERRO! Voce precisa digitar S ou N: '))

    media_idade = soma_idade / len(lista_cadastros)

print(f'A) Ao todo foram cadastradas {len(lista_cadastros)} pessoas ')
print(f'B) A media das idades foi: {media_idade:.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end = '')
for p in lista_cadastros:
     if p['sexo'] == 'F':
          print(f'{p["nome"]}', end = '')
print()
print(f'D) As pessoas que estão com a idade acima da media são: ')

for p in lista_cadastros:
     if p['idade'] > media_idade:
        for k, v in p.items():
            print(f'{k} = {v}', end = " ")
        print()

          

'''print('Cadastros finalizados!')

print(f'A) Foram cadastradas {contador_pessoas} pessoas')

print(f'B) media das idades é de {media_idade}')

if len(lista_mulheres) == 0:
    print('C) Nenhuma mulher foi cadastrada')
else:
     print(f'C) As mulheres cadastradas foram {lista_mulheres_final}')

print(f'D) As idades acima da media foram: {lista_acima_media}')

print('<<PROGRAMA ENCERRADO>>')'''