jogador = {}
gols = []
soma_gols = 0


jogador['Nome'] = str(input('Qual o nome do jogador?'))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
jogador['Partidas'] = partidas

for partida in range(partidas):
        gols_feitos = int(input(f'Quantos gols foram feitos na {partida+1} partida'))
        soma_gols += gols_feitos
        gols.append(gols_feitos)


jogador['Gols Feitos'] = gols
jogador['Total Gols'] = soma_gols


print('=-' * 30)

print(jogador)

print('=-' * 30)

for k, v in jogador.items():
    print(f'{k}:{v}')

print('=-' * 30)

'''print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} jogos')
for partida in range(partidas):
    print(f' => Na partida {partida+1} ele fez {gols_feitos}')
print(f'Foram um total de {soma_gols} gols.')'''

print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} jogos')
partidas_jogadas = []
partidas_jogadas = jogador['Partidas']
partidas_jogadas = jogador['Gols Feitos']

for i, g in enumerate(partidas_jogadas):
    print(f'Na partida {i+1} ele marcou {g} gols')
print(f'Foi um total de {soma_gols} gols')

