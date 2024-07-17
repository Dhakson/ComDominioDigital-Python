"""n = int(input('Digite um Número:'))
for c in range(1,11):
    print(f'{n} x {c} = ', n*c)"""


def calculadora():
    n = int(input('Digite um número: '))
    for c in range(11):
        print(f"{n} x {c} = ",n*c)

calculadora()