palavras = ('arroz', 'feijao', 'batata', 'macarrao', 'carne', 'frango', 'futebol', 'familia')
for palavra in palavras:
    print(f'\nA palavra {palavra.upper()} possui as vogais',  end =' ' )
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end =' ')

