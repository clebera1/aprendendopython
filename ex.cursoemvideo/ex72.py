cont = 'zero','um', 'dois', 'tres', 'quatro' , 'cinco' , 'seis', 'sete', 'oito' , 'nove', 'dez'



while True:
    numero = int(input('Digite um numero entre 0 e 10: '))
    
    if 0 <= numero <= 10:
        break
    print('Tente novamente. ', end = '')
print(f'O numero que voce digitou foi o {cont[numero]}')