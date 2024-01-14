def metade(preço = 0, formatar = False): 
    res = preço / 2     
    return res if formatar is False else moeda(res)

def dobro(preço = 0, formatar = False):
    res = preço * 2
    return res if not formatar else moeda(res)

def aumentar(preço = 0, porcentagem = 0, formatar = False):
    res =  preço + preço * (porcentagem / 100)
    return res if formatar is False else moeda(res)

def diminuir(preço = 0, porcentagem = 0, formatar = False):
    res = preço - preço * (porcentagem / 100)  
    return res if not formatar else moeda(res)

def moeda(preço = 0, moeda = 'R$', formatar = False):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def resumo(preço, aumento, diminuição):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:  {moeda(preço)}')
    print(f'Dobro do preço: {dobro(preço, True)}')
    print(f'Metade do preço: {metade(preço, True)}')
    print(f'{aumento}% de aumento: {aumentar(preço,aumento,True)}')
    print(f'{diminuição}% de redução: {diminuir(preço,diminuição,True)}')
    print('-' * 30)

