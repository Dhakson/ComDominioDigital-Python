#Solicite ao usuário um número de 1 a 12 e mostre o nome do mês correspondente.
# Caso o mês não exista, mostre valor "INVALIDO"

usuario = int(input('Digite um número de 1 a 12  : '))

if usuario <=12 and usuario > 0 :
    if usuario == 1:
            print('Você Selecionou o Mês de Janeiro')
    elif usuario == 2:
            print('Você Selecionou o Mês de Fevereiro')
    elif usuario == 3:
            print('Você Selecionou o Mês de Março')
    elif usuario == 4:
            print('Você Selecionou o Mês de Abril')
    elif usuario == 5:
            print('Você Selecionou o Mês de Maio')
    elif usuario == 6:
            print('Você Selecionou o Mês de Julho')
    elif usuario == 7:
            print('Você Selecionou o Mês de Junho')
    elif usuario == 8:
            print('Você Selecionou o Mês de Agosto')
    elif usuario == 9:
            print('Você Selecionou o Mês de Setembro')
    elif usuario == 10:
            print('Você Selecionou o Mês de Outubro')
    elif usuario == 11:
            print('Você Selecionou o Mês de Novembro')
    elif usuario == 12:
            print('Você Selecionou o Mês de Dezembro')

else:
    print(f'Você digitou o número {usuario} não existe em nosso calendário \nValor Invalido')