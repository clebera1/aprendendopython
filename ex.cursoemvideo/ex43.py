peso = float(input('Qual o seu peso em em KG? ')) 
altura = float(input('Qual sua altura em metros? '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >=25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc > 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Morbida')
else: 
    print('ERRO')