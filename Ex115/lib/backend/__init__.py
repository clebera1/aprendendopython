from time import sleep
from Ex115.lib.frontend import *

'''def criarArquivo(arquivo, modo = 'w'):
    criar = open(arquivo, modo)
    print('Criando...')
    sleep(0.8)
    print(f'Arquivo {arquivo} criado com sucesso!')
    return criar

def abrirArquivo(arquivo, modo = 'r'):
    abrir = open(arquivo, modo)
    print(f'Abrindo {arquivo}')
    sleep(0.4)
    return abrir

def lerArquivo():
    pessoas_cadastradas = open('Pessoas Cadastradas.txt', 'r')
    print(pessoas_cadastradas.read())

def cadastrarPessoas():'''

def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        print(f'Arquivo {arquivo} aberto com sucesso')
        return True
    
def criarArquivo(arquivo):
    try:
        a = open(arquivo, 'w')
        a.close()
    except:
        print('Houve um problema com o arquivo')
    else:
        print(f'Arquivo {arquivo} criado com sucesso')

def lerArquivo(arquivo):
    try:
        a = open(arquivo, 'r')
    except:
        print('Houve um erro na leitura do arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>} anos')
    finally:
        a.close()

def cadastrarPessoas(arquivo, nome = 'desconhecido', idade = 0):
    
    
    try:
        a = open(arquivo, 'a')
    except:
        print('Houve um erro na abertura do Arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
            
        except:
            print('Houve um erro ao escrever os dados')

        else:
            print(f'Novo registro de "{nome}" adicionado!')