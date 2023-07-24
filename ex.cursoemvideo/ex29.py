vel = int(input('Qual a velocidade do carro: '))
multa = (vel - 80) * 7



if vel > 80:
    print(f'Voce foi multado! o limite de velocidade é 80Km/H. Voce passou a {vel}Km/h. Sua multa será de {multa} R$')
elif vel < 80:
    print(f'Voce passou a {vel} e esta dentro do limite de 80Km/H. Tenh aum bom dia!')
else:
    print(f'Quase!! Voce passou a 80km/h, este é o limite! Dirija com segurança')