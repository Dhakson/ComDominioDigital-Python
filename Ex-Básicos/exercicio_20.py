n = divisao = 0
for c in range(3):
    nota = int(input(f'digite a {c+1}ª nota: '))
    if nota >= 0 and nota <= 10:
        n += nota
        divisao += 1

if divisao != 0:
    media = n / divisao
    print(media)
else:
    print('Nota Incorreta')