"""Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada lista em um array diferente
após completar a digitação, imprimir nome,senha e posição dos dados no array"""


nomes = [""]
senhas = [0]

for c in range(1):
    nomes[c] = input("Digite o Nome: ")
    senhas[c] = int(input("Digite a senha: "))

for x in range(1):
    print(f"\nPosição {x}: \nUsuário: {nomes[x]} \nsenha:{senhas[x]}")

