matriz = [[0,0,0],[0,0,0], [0,0,0]]
soma_total = soma_coluna_3 = maior = contador = 0
for lin in range(0,3):
    for col in range(0,3):
        matriz[lin][col] = int(input(f'Digite um numero para a posição [{lin},{col}]: '))
        if matriz[lin][col] % 2 == 0:
            soma_total += matriz[lin][col]
        soma_coluna_3 += matriz[lin][2]
        if contador == 0:
            maior = matriz[1][col]
        else:
            if matriz[1][col] > maior:
                maior = matriz[1][col]
        contador += 1

#Mostrar a matriz na tela
for lin in range(0,3):
    for col in range(0,3):
        print(f'[{matriz[lin][col]:^5}]', end = '')
    print()
print(f'A soma de todos os numeros pares é igual a {soma_total}')
print(f'A soma dos numeros da coluna 3 é igual a {soma_coluna_3}')
print(f'O maior valor da linha 2 é o numero {maior}')