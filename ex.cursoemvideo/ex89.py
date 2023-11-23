'''''

Primeira tentativa

alunos = []
boletim = []
status = ''

print('Estou aqui para te ajudar com seu Boletim. Por favor, siga as instruções: ')
while True:
    nome = str(input('Digite o nome do Aluno: ').upper())
    nota1 = float(input('Qual a nota da primeira prova? '))
    nota2 = float(input('Qual a nota da segunda prova? '))
    media = (nota1 + nota2) / 2

    
    alunos.append(nome)
    alunos.append(nota1)
    alunos.append(nota2)
    alunos.append(media)
    if media > 6:
        status = "Aprovado"
    else:
        status = "Reprovado"
    alunos.append(status)
    boletim.append(alunos[:])

    alunos.clear()
    resp = str(input('Deseja continuar? ')[0])
    if resp not in 'Ss':
        break

print('Abaixo estão os alunos e suas respectivas médias')

print('No.   NOME     MEDIA    Status')
print('-' * 30) 

for indice, aluno in enumerate(boletim):
    print(f'{indice+1}     {aluno[0]}    {aluno[3]}      {aluno[4]}')



while True: 
    busca = str(input('Digite o aluno que quer buscar. [999 caso queira parar.]:'))
    for i,l in enumerate(boletim):
        if boletim[i][0] == busca:
            print(f'As notas de {boletim[i][0]} foram: {boletim[i][1]} e {boletim[i][2]}')
    if busca == '999':
        break
print('Programa encerrado!')



#continuar a partir daqui, consegui fazer com que buscasse o indice certo. agora preciso trazer as notas das provas!!!'''

lista = []

print('Estou aqui para te ajudar com seu boletim. Vamos lá:')

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar? [S/N]')[0].upper())
    if resp not in "Ss":
        break
print(f'{"No":<4} {"Aluno":<10} {"Media":>8}')

for i, a in enumerate(lista):
    print(f'{i:<4} {a[0]:<10}  {a[2]:<8}')

while True:
    busca = int(input('Procurar aluno pelo ID (999 interrompe): '))
    if busca == 999:
        break
    if busca <= len(lista) - 1:
            print(f'As notas do aluno {lista[busca][0]} foram {lista[busca][1]}')

print('Programa finalizado')