jogadores = {
    'luciano': 'sao paulo',
    'veiga': 'palmeiras',
    'roger guedes': 'corinthians',
    'suarez': 'gremio',    
    'marcelo': 'fluminense'
}

for time in jogadores.values():
    print(time)

for time in jogadores.items():
    print(time)
    
print(jogadores['marcelo'])