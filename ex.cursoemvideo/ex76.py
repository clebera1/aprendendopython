print('-' * 30)
print('LISTAGEM DE PREÇOS')
print('-' * 30)

materiais = ('Lapis', 1.75,
             'Borracha', 2.30,
             'Caneta', 5.0,
             'Bolsa', 10.0,
             'Mochila', 45.50)
for pos in range(0, len(materiais)):
    if pos % 2 == 0:
        print(f'{materiais[pos]:.<30}', end = '')
    else:
        print(f'R${materiais[pos]:>3.2f}')
