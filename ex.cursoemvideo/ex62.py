primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(termo, end= '->')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais voce quer mostrar?'))
print('fim')
print(f'Foram mostrados um total de {total} termos')

    

