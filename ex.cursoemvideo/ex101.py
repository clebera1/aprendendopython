def vota(nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - nascimento
    if idade < 16:
        return f'Com {idade} anos voce não vota!'
    elif idade >= 16 and idade < 18 or idade >= 65:
        return f'Com {idade} anos seu voto é opcional!'
    else:
        return f'Com {idade} anos seu voto é obrigatorio!'


ano_nasceu = int(input('Qual ano voce nasceu? '))
print(vota(ano_nasceu))