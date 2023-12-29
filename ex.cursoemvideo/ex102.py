def fatorial(num, show=False):
    """
    Função recebe dois parametros:
    num: numero a ser calculado
    show=False: valor logico e opcional que indica se sera mostrado na tela ou nao o processo de calculo do fatorial
    return: retorna o resultado do fatorial do numero digitado
    """
    f = 1
    for c in range(num, 0, -1):
  
        if show:
            print(c, end = '')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
        f*=c
    return f

numero = int(input('Digite um numero e saiba seu fatorial: '))
print(fatorial(numero, True))

help(fatorial)
    


