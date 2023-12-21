from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    
    print(f'Contando de {inicio} a {fim} de {passo} em {passo}')
    sleep(0.5)
    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print(cont, end= ' ', flush= True)
            cont += passo
            sleep(0.2)
        print('Fim!')
    else:
        while cont >= fim:
            print(cont, end= ' ', flush=True)
            cont -= passo
            sleep(0.2)
        print('Fim!')


contador(1,10,1) 
contador(10, 0, 2)
print('Agora é sua vez: ')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i, f, p)