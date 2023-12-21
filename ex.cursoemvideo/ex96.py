def area(l, c):
    area = l * c
    print(f'A area do terreno com as dimensões: Largura {l} e Comprimento {c} é de {area}m2')

largura = float(input('Qual a largura do terreno? '))
comprimento = float(input('Qual o comprimento do terreno? '))

area(largura, comprimento)