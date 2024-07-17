"""Criar um array tamanho 5 e preencher com os nomes dos alunos, informados pelo usuario"""

nomes = ["","","","",""]

for c in range(len(nomes)):
    nomes[c] = input("Digite o nome: ")

for x in range(len(nomes)):
    print(f"Posição {x} está o nome {nomes[x]}")