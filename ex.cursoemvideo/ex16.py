import math
co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjacente: '))
hipotenusa = (co **2) + (ca**2) 
print(f'Com esses valores dos catetos a hipotenusa irá medir {math.sqrt(hipotenusa)}')

