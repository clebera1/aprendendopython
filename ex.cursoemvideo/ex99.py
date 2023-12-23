def verifica_maior(*num):
    contador = 0
    for n in num:
        if contador == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        contador+=1

    if len(num) == 0:
        maior = 0
    
    for n in num:
        print(n, end = ' ')
    print(f'Analisando os valores passados....')
    print(f'Foram informados {len(num)} valores ao todo. O maior valor informado foi o {maior}')
    print()



verifica_maior(2,6,4,3,1,8,9,0)
verifica_maior(67)
verifica_maior(0,29,45,1)
verifica_maior(4,7,0)
verifica_maior()