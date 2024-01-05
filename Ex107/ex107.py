import moeda
preço = float(input('Digite o preço: R$ '))
print(f'A metade de {preço} é {moeda.metade(preço)}')
print(f'O dobro de {preço} é {moeda.dobro(preço)}')
print(f'Se aumentarmos {preço} em 10% o valor seria {moeda.aumentar(preço, 10)}')
print(f'Se diminuirmos {preço} em 13% o valor seria de {moeda.diminuir(preço, 13)}')