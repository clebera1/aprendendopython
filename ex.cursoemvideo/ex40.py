n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print(f'Sua media foi de {media}, sendo assim voce esta reprovado')
elif media >= 5 and media < 7:
    print(f'Sua media foi de {media}, sendo assim voce esta de recuperação')
else: 
    print(f'Sua media foi de {media}, sendo assim voce está aprovado')