idade = int(input('Qual a sua idade:'))
if idade <= 9:
    print('Voce esta na categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('Voce esta na categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Voce esta na categoria JUNIOR')
elif idade > 19 and idade <= 25:
    print('Voce esta na categoria SENIOR')
else:
    print('Voce esta na categoria MASTER')