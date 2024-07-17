notas = [0,0,0,0,0]
soma = 0
for c in range(len(notas)):
    notas[c] = int(input(f'{c}ª nota: '))
for x in range(len(notas)):
    soma = notas[0] + notas[1] + notas[2] + notas[3]

for m in range(len(notas)):
    media = soma / len(notas)