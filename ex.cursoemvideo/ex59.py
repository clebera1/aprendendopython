
from time import sleep

'''
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
sair = False


while not sair:
    print('=-=-=-=-=-=-=-=-')
    opcao = int(input('
    [1] - somar
    [2] - multiplicar
    [3] - maior
    [4] - novos numeros
    [5] - sair do programa'))
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma dos numeros é {soma}')
    elif opcao == 2:
        mult = num1 * num2
        print(f' A multiplicação dos numeros é {mult}')
    elif opcao == 3:
        if num1 > num2:
            print(f'O numero {num1} é o maior')
        elif num1 < num2:
            print(f'O numero {num2} é o maior')
        else:
            print('Os numeros são iguais')
    elif opcao == 4:
        num1 = int(input('Digite um novo numero: '))
        num2 = int(input('Digite mais um novo numero: '))
        print('O que deseja fazer com os novos numeros? ')
    elif opcao == 5:
        print('Programa encerrando.... Volte sempre')
        sair = True
    else:
        print('Nao entendi. Escolha dentre as opções')
'''

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

opcao = 0

while opcao != 5:
    print('''    [1] - somar
    [2] - multiplicar
    [3] - maior
    [4] - novos numeros
    [5] - sair do programa''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma dos numeros é {soma}')
    elif opcao == 2:
        mult = num1 * num2
        print(f' A multiplicação dos numeros é {mult}')
    elif opcao == 3:
        if num1 > num2:
            print(f'O numero {num1} é o maior')
        elif num1 < num2:
            print(f'O numero {num2} é o maior')
        else:
            print('Os numeros são iguais')
    elif opcao == 4:
        num1 = int(input('Digite um novo numero: '))
        num2 = int(input('Digite mais um novo numero: '))
        print('O que deseja fazer com os novos numeros? ')
    elif opcao == 5:
        print('Finalizando...')

sleep(1)
print('Programa encerrando.... Volte sempre')

