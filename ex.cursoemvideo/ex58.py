from random import randint

'''print('Vou pensar em um numero. Tente adivinhar')
numero = randint(0,10)
resposta = int(input('Qual numero estou pensando?'))
acertou = False
contador = 0

while not acertou:
    resposta = int(input('Qual numero voce acha que é? '))
    if resposta > numero:
        print('Quase... Mais pra baixo')
        contador = contador + 1
        resposta = int(input('Tente novamente: '))
    elif resposta < numero:
        print('Quase.... Mais pra cima')
        contador = contador + 1
        resposta = int(input('Tente novamente: '))
    else:
        print(f'Exatamente! O numero que eu pensei foi {numero}')
        print(f'Voce precisou de {contador} chances para acertar')
        acertou = True
    '''

#variaveis
'''print('Sou o computador. Vou pensar em um numero e voce terá que adivinhar...')
computador = randint(0,10)
jogador = ''
palpites = 0

while computador != jogador:
    jogador = int(input('Qual numero acha que eu escolhi? '))
    if jogador > computador:
        print('Quase... Mais pra baixo')
        palpites += 1
    elif jogador < computador:
        print('Quase.... Mais pra cima')
        palpites += 1
    else:
        palpites += 1
        print(f'Acertou! O numero que escolhi foi o {computador}! Voce precisou de {palpites} palpitepara acertar!')'''

print('Sou o computador. Vou pensar em um numero')
print('Sera que voce consegue adivinhar qual foi? ')
computador = randint(0,10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual numero acha que escolhi? '))
    if jogador == computador:
        acertou = True
        palpites += 1
    else:
        if jogador > computador:
            print('Mais pra baixo. Tente de novo')
            palpites += 1
        elif jogador < computador:
            print('Mais pra cima. Tente de novo')
            palpites += 1
if palpites > 5:
    print(f'Até que enfim acertou! Voce precisou de {palpites} tentativas')
else:
    print(f'Parabens! Voce acertou precisando de apenas {palpites} tentativas')


