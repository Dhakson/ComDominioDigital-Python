
resp = 'S'
while resp == 'S' or resp == 's':
    nota1 = int(input('Primeira Nota: '))
    while nota1 <=0 or nota1 >= 10:
        nota1 = int(input('Número Invalido, digite novamente: '))

    nota2 = int(input('Segunda nota: '))
    while nota2 <=0 or nota2 >= 10:
        nota2 = int(input('Número Invalido, digite novamente: '))
    media = (nota1 + nota2) / 2
    print(media)

    resp = input('Quer Continuar? [S] - sim ou [N] - Não: ')
print('Finalizando o Programa...')