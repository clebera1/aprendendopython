valor = int(input('Digite o valor da casa: R$'))
salario = int(input('Qual o seu salário?'))
tempo = int(input('Em quantos anos voce pretende pagar essa casa?'))
tempo_em_meses = (tempo * 12)
valor_prestacao = valor / tempo_em_meses

print(f'Pagando essa casa em {tempo} anos o valor de cada prestação fica em {valor_prestacao:.2f}R$')    

if valor_prestacao > (salario * 0.3):
    print('Emprestimo negado')
else:
    print('Emprestimo concedido')


'''if valor > salario * 0.3:
    print('O empréstimo foi negado')
else:
    print('Empréstimo aprovado, o seu salário ')'''