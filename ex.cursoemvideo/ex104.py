def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        valor = str(input(msg))
        if valor.isnumeric():
            valor = int(valor)
            ok = True
        else:
            print('Erro! Digite um numero inteiro valido!')
        if ok == True:
            break
    return valor
    
n = leiaInt('Digite um numero: ')
print(f'O numero que voce digitou foi o {n}')