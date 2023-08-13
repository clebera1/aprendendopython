s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 == s3:
        print('Esse triangulo é EQUILATERO') 
    elif s1 != s2 != s3 != s1:
        print('Esse triangulo é ESCALENO')
    else:
        print('Esse triangulo é ISOSCELES')
else:
    print('Esses valores nao formam um triangulo!')