player_1 = input('player 1: impar ou par: ')
player_2 = 0
if player_1 == 'par':
    player_2 = 'impar'
else:
    player_2 = 'par'
print(f'player 2 = {player_2}')


player_1_numero = int(input('player 1 escolha seu numero: '))
player_2_numero = int(input('player 2 escolha seu numero: '))

print('valendo')
print(f'player 1: {player_1_numero}')
print(f'player 2: {player_2_numero}')

conta = player_1_numero + player_2_numero
print(conta)

if conta%2 == 0:
    print("o jogador que escolheu par ganhou")
else:
    print('o jogador que escolheu impar ganhou')