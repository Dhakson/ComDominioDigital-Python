nome = input('Digite seu nome: ')
idade = int(input('Digite a sua idade: '))
cidade = input('Em que cidade você mora: ')

print(f'{nome}, Seja Bem vindo ao CDD, \nvocê tem {idade} anos e mora na cidade de {cidade}')

print('\nOlá, {}  sua idade é {} \nvocê é morador da cidade de {}'.format(nome,idade,cidade))