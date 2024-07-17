nomes = ['','','']

for c in range(len(nomes)):
    nomes[c] = input('Digite um nome: ')

for x in range(len(nomes)):
    print(f'{x+1}ª Posição: {nomes[x]}')