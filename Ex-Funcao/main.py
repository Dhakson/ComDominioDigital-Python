from funcao_04 import *

nome = input("Nome do Produto: ")
quantidade = int(input("Quantidade: "))
valor_unitario = float(input("Valor Unitário R$: "))

tot = estoque(nome,quantidade,valor_unitario)
soma = 0
soma += tot
print(f'R${tot:7.2f}')
