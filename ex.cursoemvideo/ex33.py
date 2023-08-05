n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
n3 = int(input('Por fim, digite mais um numero:'))
menor = n1
maior = n3

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3

if n2>n3 and n2>n1:
    maior = n2
if n1>n2 and n1>n3:
    maior = n1
print(f'O menor numero digitado é {menor} e o maior é {maior}')
