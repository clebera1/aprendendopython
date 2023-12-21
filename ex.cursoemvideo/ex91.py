#FAZENDO VIA LISTA

'''from random import randint
from time import sleep
jogadores = []
print('Jogando os dados:')
sleep(0.5)
for i in range(1,5):
    jogador = randint(1,6)
    print(f'O jogador{i} tirou o numero {jogador}')
    sleep(0.4)
    jogadores.append(jogador)


jogadores.sort(reverse=True)

print('GERANDO A POSICAO DOS JOGADORES')
for id,dado in enumerate(jogadores):
    print(f'O jogador{id+1} foi o {id+1}Lugar e tirou {dado}')'''


#FAZENDO VIA DICIONARIO

from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'jogador 1': randint(1,6),
    'jogador 2': randint(1,6),
    'jogador 3': randint(1,6),
    'jogador 4': randint(1,6)
}
ranking = []
print("Valores sorteados:")
for key, value in jogo.items():
    print(f'O {key} jogou o dado {value}')
    sleep(0.6)

ranking = sorted(jogo.items(), key = itemgetter(1), reverse=True)


print("Ranking dos Jogadores")

for i, v in enumerate(ranking):
    print(f'O {i+1} lugar foi o {v[0]} que tirou o dado {v[1]}')
    sleep(0.6)