"""fora = dentro = 0
for c in range(5):
    n = int(input(f'Digite o {c+1}ª : '))

    if 10 <= n <= 20:
        dentro += 1
    else:
        fora += 1

print(f'Quantidade Números fora do intervalo: {fora}')
print(f'Quantidade Números dentro do intervalo: {dentro}')"""


def multiplicador():
    numero = int(input('Digite um número: '))
    for c in range(1,11):
        print(f'{numero} x {c} = ',numero * c)

def divisao():
    numero = int(input('Digite um número: '))
    for c in range(1, 11):
        print(f'{numero} / {c} = ', numero / c)


multiplicador()
divisao()