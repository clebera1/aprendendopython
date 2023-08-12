from datetime import date
nascimento = int(input('Qual ano você nasceu? ')) 
idade = date.today().year - nascimento
sexo = input('Sexo? [M ou F]: ')
def alistar():
    if idade < 18:
        print(f'Voce vai se alistar daqui {(18 - idade)} anos no ano de {date.today().year + (18 - idade)}')
    elif idade == 18:
        print(f'Esta na hora de se alistar')
    else:
        print(f'Voce precisava ter se alistado a {idade - 18} anos no ano de {date.today().year + (18 - idade)}')
if sexo.upper() == 'M':
    alistar()
elif sexo.upper() == 'F':
    escolha = input('Voce deseja se alistar? [S ou N]: ')
    if escolha.upper() == 'S':
        alistar()
    elif escolha.upper() == 'N':
        print('Tenha um ótimo dia')
    else:
        print('ERRO')
else:
    print('ERRO')



