from Ex109 import moeda


preço = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço, True)}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}')
print(f'Se aumentarmos {moeda.moeda(preço)} em 10% o valor seria {moeda.aumentar(preço, 10, True)}')
print(f'Se diminuirmos {moeda.moeda(preço)} em 13% o valor seria de {moeda.diminuir(preço, 13, True)}')