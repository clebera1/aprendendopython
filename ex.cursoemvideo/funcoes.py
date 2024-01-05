'''
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(2)
f2 = fatorial()
f3 = fatorial(5)

print(f'Os fatoriais são: {f1}, {f2} e {f3}')
'''

'''def par(n=0):
    if n%2==0:
        return True
    else:
        return False

n = int(input('Digite um numero e saiba se ele é par: '))

if par(n) == True:
    print(f'{n} é um numero par')
else:
    print(f'{n} não é um numero par')'''

def falar_oi(nome):
    print(f'Olá, {nome}')


n = str(input('Digite seu nome: '))
falar_oi(n)
