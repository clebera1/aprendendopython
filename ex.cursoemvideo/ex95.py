jogador = {}
lista_jogadores = []
partidas = []

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Qual o nome do jogador?'))
    total = int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))

    for c in range(0, total):
        partidas.append(int(input(f'Quantos gols foram feitos na {c+1} partida')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    partidas.clear()
    
    while True:
        continuar = str(input('Deseja continuar? [S / N]').upper()[0])
        if continuar in "SN":
            break
        print('ERRO! Voce deve inserir apenas S ou N')
    lista_jogadores.append(jogador.copy())
    if continuar in 'Nn':
        break



print(f'Codigo', end = ' ')
for i in jogador.keys():
    print(f' {i:<15}', end = ' ')
print()
for i,jogador in enumerate(lista_jogadores):
    print(f'{i:<3}',end = '')
    for v in jogador.values():
        print(f'{str(v):<15}', end = '')
    print()





while True:
    pesquisar = int(input('Mostrar dados de qual jogador? [999 para parar]'))
    if pesquisar ==  999:
        break
    if pesquisar >= len(lista_jogadores):
        print(f'Nao existe jogador com o codigo {pesquisar}')
    else:
        print(f'---- Levantamento do Jogador {lista_jogadores[pesquisar]["Nome"]} ----')
        for i, g in enumerate(lista_jogadores[pesquisar]["Gols"]):
            print(f'No jogo {i+1} fez {g} gols')
    
print('Programa finalizado! Volte sempre')




#Mostrar dados na tela  

''' 
print('=-' * 30)    

print(jogador)               
        
print('=-' * 30)                 
        
for k, v in jogador.items():                 
    print(f'{k}:{v}')   

print('=-' * 30)'''

'''
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} jogos')
for i, g in enumerate(jogador["Gols"]):
    print(f'Na partida {i+1} ele marcou {g} gols')
print(f'Foi um total de {jogador["Total"]} gols')
'''

