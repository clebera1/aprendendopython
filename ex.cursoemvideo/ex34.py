salario = float(input('Qual o seu salario?'))
aumento_salario_baixo = 0.15
aumento_salario_alto = 0.10
if salario >= 1250:
    salario_novo = salario + (salario * aumento_salario_alto)
else: 
    salario_novo = salario + (salario * aumento_salario_baixo)
print(f'O seu salario de {salario}R$ aumentou para {salario_novo}R$')