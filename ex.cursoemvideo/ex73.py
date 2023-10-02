times = ('botafogo', 'palmeiras', 'gremio', 'flamengo', 'bragantino', 'fluminene', 'atletico-mg', 'atletico-pr', 'fortaleza', 'sao paulo', 'cuiaba', 'cruzeiro', 'corinthians', 'internacional', 'santos', 'vasco da gama', 'goias', 'bahia', 'america mg', 'coritiba')

print(f'Os 5 primeiros times do campeonato braileiro são: {times[:5]}')
print('=-=' * 30)
print(f'Os ultimos 4 colocados são {times[-4:]}')
print('=-=' * 30)
print(f'Os times em ordem alfabetica são: {sorted(times)}')
print('=-=' * 30)
print(f'O fortaleza está na {times.index("fortaleza")} posição')