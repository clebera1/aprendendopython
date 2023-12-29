'''def ficha(jogador = '<desconhecido>', gols = 0):
    print(f'O jogador {jogador} fez {gols} gols')



#Programa Principal 
nome = str(input('Qual o nome do jogador? '))
qtd_gols = str(input('Quantos gols esse jogador fez? '))

if qtd_gols.isnumeric():
    qtd_gols = int(qtd_gols)
else:
    qtd_gols = 0
if nome.strip() == '':
    ficha(gols = qtd_gols)
else:
    ficha(nome, qtd_gols)
    
'''

#Teste de novo

def ficha(jogador = '<desconhecido>', gols = 0):
    print(f'O jogador {jogador} fez {gols} gols')

nome = str(input('Nome do jogador: '))
qtd_gols = str(input('Quantidade de gols: '))

if qtd_gols.isnumeric():
    qtd_gols = int(qtd_gols)
else:
    qtd_gols = 0

if nome.strip() == '':
    ficha(gols = qtd_gols)
else:
    ficha(nome, qtd_gols)