from datetime import date
contador_maior = 0
contador_menor = 0
atual = date.today().year 

for pessoas in range (1,8):

    nascimento = int(input(f'Em que ano a {pessoas} pessoa nasceu? '))
    idade = atual - nascimento

    if idade > 18:
        contador_maior = contador_maior + 1
    else:
        contador_menor = contador_menor + 1
print(f'Tiveram {contador_maior} pessoas de maior e {contador_menor} pessoas de menor')