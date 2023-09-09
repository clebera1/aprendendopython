print('Sequencia de fibonacci')
n = int(input('Digite quantos termos voce quer ver: '))
primeiro = 0
segundo = 1
count = 3
print(f'{primeiro} -> {segundo} ', end = '->')
while count <= n:
    atual = primeiro + segundo
    print(atual, end = ' -> ')
    primeiro = segundo
    segundo = atual
    count += 1
print('FIM')
