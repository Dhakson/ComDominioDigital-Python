qntd = soma = 0
while qntd <= 2:
    numero = int(input('Digite a nota: '))
    soma += numero
    qntd += 1

media = soma / qntd

print(f'{media:.2f}')