
'''
def notas(*notas, media, situação = False):

    notas_alunos = [2,10]
    alunos = {'Notas' : notas_alunos}

    c = maior = menor =0
    for n in notas_alunos:
        if c == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        c+=1
    media = sum(notas_alunos) / len(notas_alunos)
    print(media)
    print(alunos)

respostas = notas()
'''
alunos = {}


def notas(*notas , situação = False):
    """
    função notas: recebe as notas dos alunos e calcula media, mostra maior e menor alem de falar sua situação
    parametro notas: receba as notas dos alunos
    parametro situação: recebe a situação, pode ser false ou true (Opcional)
    """



    maior = menor = contador = 0
    alunos['total'] = len(notas)
    for n in notas:
        if contador == 0:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            elif n < menor:
                menor = n
        contador += 1
    alunos['maior'] = maior
    alunos['menor'] = menor
    alunos['media'] = sum(notas) / len(notas)
    if situação:
        if alunos['media'] >= 8:
            alunos['situação'] = 'BOM'
        elif alunos['media'] >= 5 and alunos['media'] < 8:
            alunos['situação'] = 'RAZOAVEL'
        else:
            alunos['situação'] = 'RUIM'
    

        



            
    return alunos

resposta = notas(2,0,10,8,0, situação = True)
print(resposta)