from datetime import date

ano_atual = date.today().year

pessoa = {}

pessoa['Nome']= str(input('Qual o seu nome?'))

nascimento = int(input('Qual ano voce nasceu?'))

pessoa['CPTS'] = int(input('Qual sua carteira de trabalho? (Digite 0 caso nao tenha)'))

if pessoa['CPTS'] == 0:
    print('Nunca trabalhou, banco de dados vazio')
else:
    idade = ano_atual - nascimento
    pessoa['idade'] = idade
    pessoa['Ano de Contratação:'] = int(input('Em qual ano voce foi contratado? '))
    pessoa['Salário'] = float(input('Qual o seu salário? '))

    

    idade_aposentadoria = idade + pessoa['Ano de Contratação:'] + 35 - ano_atual

    pessoa['Idade da Aposentadoria'] = idade_aposentadoria
 

    for k, v in pessoa.items():
        print(f'{k}:{v}')