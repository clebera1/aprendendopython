import random

contador = 0

print('=-=' * 10)
print('Vamos jogar par ou impar')
print('=-=' * 10)
while True:
    jogador = int(input('Digite um valor: '))
    par_ou_impar = str(input('Par ou impar? [P/I]: ')[0]).upper()
    computador = random.randint(0, 10)
    total = jogador + computador
    print(f'O jogador jogou {jogador} e o computador jogou {computador}. Dando um total de {total}')
    if total % 2 == 0 and par_ou_impar == 'P':
        print('Voce venceu! Vamos jogar de novo...')
        contador += 1
    elif total % 2 != 0 and par_ou_impar == 'I':
        print('Voce venceu! Vamos jogar de novo...')
        contador =+ 1
    else:
        print('Voce perdeu!')
        break
print(f'Game Over! Voce venceu um total de {contador} vezes!')