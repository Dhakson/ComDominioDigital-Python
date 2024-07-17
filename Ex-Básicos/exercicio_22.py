qntd_aluno = int(input("Quantidade de Alunos: "))
qntd = 0
soma = 0
while qntd < qntd_aluno:
    notas = int(input('Digite as notas: '))
    qntd += 1
    soma += notas

media = soma / qntd_aluno

print(f"A media {media} da sala de {qntd_aluno} Alunos")