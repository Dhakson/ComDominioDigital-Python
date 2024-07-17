""""Escreva um código que permita a leitura das notas de uma turma de 5 alunos e guarde num vetor,
 calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calaculada escrever
 a média da turma e o resultado da contagem"""

notas = [0,0,0,0,0]
soma = 0
acimamedia = 0
for c in range(len(notas)):
    notas[c] = float(input(f"Digite a {c+1}ª Nota => "))

for x in range(len(notas)):
    soma += notas[x]
media = soma / len(notas)

