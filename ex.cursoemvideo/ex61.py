'''print('Os 10 primeiros termos de uma PA: ')

primeiro_termo = int(input('Qual será o primeiro termo de sua PA? '))

razao = int(input('Qual será a razão de sua PA? '))

decimo_termo = primeiro_termo + 10 * razao

c = primeiro_termo

while c != decimo_termo:
    print(c, end = '->')
    c = c + razao
print('ACABOU')'''

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão:'))
termo = primeiro_termo
contador = 1
mais_termos = 1
while contador <= 10:
    print(termo, end = '->')
    termo += razao
    contador+=1
print('fim')




