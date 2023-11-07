lista = []

for v in range(0,5):
    numero = int(input('Digite um valor: '))
    if v == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Valor adicionado na ultima posição')
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos,numero)
                print(f'Valor adicionado na posição {pos+1}')
                break 
            pos +=1
                    
print(f'Os valores digitados em ordem foram {lista}')


#fazer variaveis ''primeiro, segundo, terceiro, quarto, quinto''
#fazer method insert na posicao especifica
