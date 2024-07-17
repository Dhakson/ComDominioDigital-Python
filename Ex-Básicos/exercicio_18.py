qntdnegativo = 0
for c in range(1,4):
    n = int(input(f'{c}ª Número inteiro : '))
    if n < 0:
        qntdnegativo += 1

if qntdnegativo > 1:
    print(f'Existem {qntdnegativo} números negativos  ')
else:
    print(f'Existe {qntdnegativo} número negativo ')