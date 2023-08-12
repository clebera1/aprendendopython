numero = int(input('Digite um numero inteiro: '))
print('''Pressiona para converter em:
[1] Binário
[2] Octal
[3] Hexadecimal''')
opcao = int(input('Qual a sua escolha? '))

if opcao == 1:
    print(f'{numero} em binario é: {bin(numero)[2:]}')
elif opcao ==2:
    print(f'{numero} convertido para octal é: {oct(numero)[2:]}')
elif opcao ==3:
    print(f'{numero} em hexadecimal é: {hex(numero)[2:]}')
else: 
    print('Opção invalida')