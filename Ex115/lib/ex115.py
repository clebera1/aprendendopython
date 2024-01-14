from Ex115.lib.frontend import *
from Ex115.lib.backend import *
from time import sleep

'''try:
    abrirArquivo('Pessoas Cadastradas.txt')
except:
    criarArquivo('Pessoas Cadastradas.txt')'''
arquivo = 'Pessoas Cadastradas.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arquivo)


    elif resposta == 2:
        cabeçalho('CADASTRAR PESSOAS')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrarPessoas(arquivo, nome, idade)

    elif resposta == 3:
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('ERRO! Insira uma opção válida.')
    sleep(1)

