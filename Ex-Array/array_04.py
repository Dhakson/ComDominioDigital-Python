"""Faça um código para ler 5 números e armazenar em um vetor. Após a leitura total dos 5 números
o código deve escrever esses 5 números lidos na ordem inversa."""


numeros = [0,0,0,0,0]

for c in range(5):
    numeros[c] = int(input(f"Digite um número => "))

for x in range(4,-1,-1):
    print(numeros[x])