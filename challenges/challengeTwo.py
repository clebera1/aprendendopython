"""my_number= int(input("Enter a number: "))
if my_number < 5:
    print('Your number is less than 5')
elif my_number > 5:
    print('Your number is greater than 5')
else: 
    print('Your number is five')
if my_number > 0 and my_number < 10:
    print("single digit")
else:
    print("double digit")"""

#Pedra, Papel, Tesoura

player_1 = input('Player 1:')
print(player_1)
player_2 = input('Player 2:')
print(player_2)

if player_1 == player_2:
    print('empate')
elif player_1 == 'paper' and player_2 == 'rock':
    print('player 1 wins')
elif player_1 == 'paper' and player_2 == 'scissors':
    print ('player 2 wins')
elif player_1 == 'rock' and player_2 == 'scissors':
    print('player 1 wins')
elif player_1 == 'rock' and player_2 == 'paper':
    print ('player 2 wins')
elif player_1 == 'scissors' and player_2 == 'paper':
    print('player 1 wins')
elif player_1 == 'scissors' and player_2 == 'rock':
    print ('player 2 wins')
else:
    print('Something went wrong. Please try again')


