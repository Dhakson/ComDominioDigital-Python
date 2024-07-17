nome = input('Nome do Aluno: ')
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
n3 = float(input('Terceira Nota: '))

media = (n1+n2+n3) / 3
print(f'A media do aluno {nome} é :{media:.2f}')

if media >= 7:
    print('Aprovado')
elif media <= 4:
    print('Reprovado')
else:
    print('Recuperação')