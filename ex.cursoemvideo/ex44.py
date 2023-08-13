preco = int(input('Qual o preco do seu produto?'))

def pagamento():
    global preco
    print(''' Formas de Pagamento:
      [1] A vista (Dinheiro)
      [2] A vista (Cartão)
      [3] 2x no Cartão
      [4] 3x ou mais no Cartão''')
    opcao = int(input('Como gostaria de pagar? '))
    if opcao == 1:
        preco = preco - (preco * 0.1)
        print(f'Sua compra irá ficar no valor de {preco}')
    elif opcao == 2:
        preco = preco - (preco * 0.05)
        print(f'Sua compra ira ficar no valor de {preco}')
    elif opcao == 3:
        print(f'Sua compra ira ficar em 2 vezes de {preco / 2}')
    elif opcao == 4:
        parcela = int(input('Em quantas parcelas voce irá fazer? '))
        if parcela <= 2:
            print(f'Sua compra ira ficar em 2 vezes de {preco / 2}')
        else:
            print(f'Sua compra ira ficar em {parcela} vezes de {(preco + (preco * 0.2)) / parcela}')
            print(f'de {preco} essa compra irá custar {preco + preco * 0.2}')
    else: 
        print('Erro, escolha uma das opções:')
        pagamento()
pagamento()



