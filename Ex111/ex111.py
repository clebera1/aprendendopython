from UtilidadesCeV import moeda, dado


while True:
    preço = dado.leiaDinheiro('Digite o preço: R$ ')
    increase = dado.leiaDinheiro('Quanto será o valor do aumento?')
    decrease = dado.leiaDinheiro('Quanto será o valor da redução?')
    moeda.resumo(preço, increase, decrease)
    continuar = str(input('Deseja continuar? ').upper()[0])
    if continuar in 'Nn':
        break
print('Programa encerrado!')
'''print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço, True)}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}')
print(f'Se aumentarmos {moeda.moeda(preço)} em 10% o valor seria {moeda.aumentar(preço, 10, True)}')
print(f'Se diminuirmos {moeda.moeda(preço)} em 13% o valor seria de {moeda.diminuir(preço, 13, True)}')'''
