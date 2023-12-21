dicionario = {}
dicionario = {
    'nome': str(input('Qual o seu nome?')),
    'media': int(input(f'A media foi: ')),
    }
if dicionario['media'] > 7:
    dicionario['situacao'] = 'aprovado'
else:
    dicionario['situacao'] = 'reprovado'

for chave, valor in dicionario.items():
    print(f'O {chave} é {valor}')
