#Final Project - Password Checker

import string

#Get password input 

def verifica_senha():

    senha = input('Escolha uma senha:')
    

    #trasnform the variable "senha" in a list of letter and put it in a variable called "lista_senha"
    lista_senha = list(senha)

    #create a list to check the letters within the list
    qualifications = [ 'lowercase' , 'uppercase' , 'number', 'special caracter']

    lower = 0
    upper = 0
    number = 0
    special_caracter = 0


    #loop to verify the requirements of the password

    for caracter in lista_senha: # for each letter in 'lista_senha'
        if caracter in string.ascii_lowercase: #verify if there's lowercase in the lista_senha
            lower += 1
            if 'lowercase' in qualifications: #if there's lowercase on the qualifications list it will be removed
                qualifications.remove('lowercase')
        elif caracter in string.ascii_uppercase:
            upper += 1
            if 'uppercase' in qualifications:
                qualifications.remove('uppercase')
        elif caracter in string.digits:
            number +=1
            if 'number' in qualifications:
                qualifications.remove('number')
        else:
            special_caracter += 1
            if 'special caracter' in qualifications:
                qualifications.remove('special caracter') 

        
    if len(lista_senha) <= 9:
        print('Your password is not strong enough: 9 caracters at least') 

    if len(qualifications) != 0:
        print(f"the following requirements are not met: {', '.join(qualifications)}")

    if len(qualifications) == 0 and len(lista_senha) > 9:
        print(f'Congrats, your password met all the requirements: {lower} lowercases, {upper} uppercases, {number} numbers and {special_caracter} special caracters')
    

    nova_senha = input('continuar criando senha? ')
    if nova_senha == 'sim':
        verifica_senha()
    elif nova_senha == 'nao':
        print('certo, volte mais tarde')
    else:
        print('não entendi')
        verifica_senha()

verifica_senha()




'''    if len(lista_senha) <= 9: # if the lista_senha under than 9 the passwrd is not created
        

    if len(qualifications) != 0: #if the qualifications list is not ZERO, it means, if there's any requirement to be met the system will not created the password 
        # here the system will show you which requirements are not met, the join fucntion you get the requirements from the qualification list, show them and separar each one por virgulas
'''
    



        

'''def verificar_senha():
        verificacao = []
        for caracter in verificacao:
            if caracter.islower():
                True
            elif caracter.isupper():
                True
            else:
                False

    if verificar_senha() == False:
        print('Escolha outra senha')'''