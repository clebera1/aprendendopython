import random
from time import sleep

#Pedra, papel e tesoura




print('======================== JOKENPO ==========================')
print('Voce será o Player 1, escolha entre pedra, papel ou tesoura')


player_1 = input('Sua escolha é: ')
util = ['pedra', 'papel', 'tesoura']
random.shuffle(util)
player_2 = util[0]
print(f'A escoha do computador foi: {player_2}')
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('===' * 7)

if player_1 == player_2:
        print('EMPATE')

elif player_1 == 'tesoura'  and player_2 == 'pedra':
        print('Voce perdeu')

elif player_1 == 'tesoura' and player_2 == 'papel':
        print('Voce venceu')

elif player_1 == 'papel' and player_2 == 'pedra':
        print('Voce venceu')

elif player_1 == 'papel' and player_2 == 'tesoura':
        print('Voce perdeu')

elif player_1 == 'pedra' and player_2 == 'papel':
        print('Voce perdeu')

elif player_1 == 'pedra' and player_2 == 'tesoura':
        print('Voce venceu')
else:
        print('jogada invalida')


