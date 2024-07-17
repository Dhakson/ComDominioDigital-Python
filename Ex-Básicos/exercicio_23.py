"""n1 = int(input('Digite um número: '))
n2 = int(input('Digite um outro número: '))
cont = 1

while cont > n2:
    print('Digite um número diferente de zero')
    n2 = int(input('Digite um outro número: '))

divisao = n1 / n2

print(divisao)"""

n1 = int(input('Digite um número: '))

while True:
    n2 = int(input('Digite um outro número: '))

    if n2 != 0:
        break
    else:
        print('Digite um número maior que zero')

divi = n1 / n2

print(divi)