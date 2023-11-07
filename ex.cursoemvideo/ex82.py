exp = str(input('Digite uma expressão: '))
pilha = []
for carac in exp:
    if carac == '(':
        pilha.append('(')
    elif carac == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Essa expressão é valida')
else: 
    print('Essa expressão não é valida')

