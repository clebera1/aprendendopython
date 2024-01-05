from Ex108 import moeda


preço = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'Se aumentarmos {moeda.moeda(preço)} em 10% o valor seria {moeda.moeda(moeda.aumentar(preço, 10))}')
print(f'Se diminuirmos {moeda.moeda(preço)} em 13% o valor seria de {moeda.moeda(moeda.diminuir(preço, 13))}')