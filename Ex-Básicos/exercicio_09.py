litro = float(input('Quantidade de Litro: '))
combustivel = input('Qual é o tipo de Combustivel [e]- Etanol ou [g] Gasolina: ')
g = 5.80
e = 4.90

if combustivel == 'e' or combustivel == 'E':
    total = litro * e
    print(f'Valor total a ser pago R${total:7.2f}')
elif combustivel == "g" or combustivel == 'G':
    total = litro * g
    print(f'Valor total a ser pago R${total:7.2f}')
else:
    print('Opção Invalida')