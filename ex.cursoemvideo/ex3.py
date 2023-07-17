'''x = input('digite um numero: ') 
if x.isnumeric() == True:
    print(f'{x} é um valor numerico')
else:
    print(f'{x} não é um valor numerico')'''

x = input('Digite um valor')
print(f'O tipo primitivo desse valor é {type(x)}')
print(f'Esse valor é numerico? {x.isnumeric()}')
print(f'Esse valor é alfabetico?{x.isalpha()}')
print(f'Esse valor só tem espaços? {x.isspace()}' )
print(f'Esse valor é alfanumerico? {x.isalnum()}')
print(f'Esse valor esta em letras maisculas?{x.isupper()}')
print(f'Essew jnumero esta em minusculas {x.islower()}')
print(f'esse valor esta capitalizado? {x.istitle()}')