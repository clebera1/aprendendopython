c = ''
while c in 'Ss':
    try:
        a = int(input('Digite um numero: '))
        b = int(input('Digite outro numero: '))
        resultado = a / b
    except ZeroDivisionError:
        print(f'Não é possivel dividir por 0')
    except ValueError:
        print('Houve um erro com o tipo de dados que voce inseriu')
    else:
        print(f'O resultado da divisão de {a} por {b} é {resultado:.2f}')
    finally:
        c = str(input('Deseja continuar?').upper()[0])
    if c in "Nn":
        break