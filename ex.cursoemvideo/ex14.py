km = float(input('Quantos Km vc andou com o carro? '))
dias = int(input('Quantos dias voce ficou com o carro alugado? '))

preco_km = km * 0.15
dias_preco = dias * 60

preco_final = preco_km + dias_preco
print(f'o preco que vc precisa pagar pelo aluguel do carro é de {preco_final} reais')