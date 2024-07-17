#Laços de repetições com FOR
numero = 0

for c in range(0,10):
    numeros = int(input(f'Digite o {c+1}ª: '))
    numero += numeros
total = numero
print(f'A soma total dos números é {total}')