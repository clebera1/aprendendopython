distancia = float(input('Qual a distancia em Km da viagem que você vai fazer?'))

preco_curto = 0.5
preco_longo = 0.45

if distancia > 200:
    print(f'O preco da sua viagem é de {distancia * preco_longo}')
else:
    print(f'O preco da sua viagem é de {distancia * preco_curto}')