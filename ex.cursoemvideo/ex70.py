total_gasto = produtos_mais_que_mil = contador = preco_produto_mais_barato = 0
produto_mais_barato = ''
while True:
    nome_produto = str(input('Qual o nome do produto? '))
    preco_produto = float(input('Qual o preço do produto? '))


    if contador == 0:
        preco_produto_mais_barato = preco_produto
        produto_mais_barato = nome_produto
    else:
        if preco_produto < preco_produto_mais_barato:
            produto_mais_barato = nome_produto


    if preco_produto > 1000:    
        produtos_mais_que_mil += 1
    total_gasto += preco_produto
    contador += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar comprando? [S/N]').strip().upper()[0])
    if continuar == 'N':
        break
print(f'O total gasto foi de {total_gasto}')
print(f'{produtos_mais_que_mil} produtos custam mais que 1000 reais')
print(f'{produto_mais_barato} é o produto mais barato')
