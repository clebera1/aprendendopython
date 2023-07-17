'''numbers = [0,1,2,3,4,5,6]

for number in numbers: 
    number = number *2
    print(number)
'''
'''
counter = 0 

while counter < 10:
    counter = counter + 1
    print(counter)'''
'''
items = ['steak', 'apple', 'bread', 'butter', 'pineapple']

for item in items:
   if item == 'apple' or item == 'pineapple':
      print(f'{item} is a fruit')
   else:
      print(f'{item} is not a fruit')



counter = 1 

while counter < 1000:
    counter = counter * 2
    print(counter)'''
'''
while True:
    counter = counter * 2
    print(counter)
    if counter > 1000:
        break
'''
'''import string 
senha = input('Digite sua senha: ')

lista_senha = list(senha)

print (lista_senha)

teste = ['numero', 'letra']

for char in lista_senha:
    if char in string.digits:
        print('tem numero na sua senha')
    elif char in string.ascii_letters:
        print('tem letras na sua senha')
'''

tentativa = 0



while True:
    senha = input('digite sua senha')
    if len(senha) > 2:
        print('senha criada')
        break
    else:
        print('digite sua senha novamente')

