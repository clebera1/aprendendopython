import random
a1 = str(input('digite o primeiro aluno: '))
a2 = str(input('digite o segundo aluno: '))
a3 = str(input('digite o terceiro aluno: '))
a4 = str(input('digite o quarto aluno: '))

lista = [a1,a2,a3,a4]
random.shuffle(lista)


print(f'A ordem de apresentação do trabalho será a seguinte:')
for item in lista:
    print(item)