nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'A media desse aluno foi de {media}')

if media > 6:
    print('Esse aluno passou')
else:
    print('Esse aluno reprovou')