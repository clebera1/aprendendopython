import math
angulo = int(input('Digite o angulo que voce quer: '))

cos = math.cos(math.radians(angulo))
print(f'a valor do cosseno de {angulo} é {cos:.2f}')

sen = math.sin(math.radians(angulo))
print(f'o valor do sen de {angulo} é {sen:.2f}')

tan = math.tan(math.radians(angulo))
print(f'O valor da tangente de {angulo} é {tan:.2f}')