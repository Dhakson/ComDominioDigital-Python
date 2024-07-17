
vetor_A = [0,0,0,0,0,0,0,0,0,0]
vetor_M = [0,0,0,0,0,0,0,0,0,0]
for c in range(len(vetor_A)):
    vetor_A[c] = int(input(f"Digite um número {c}ª => "))

multiplicador = int(input("Digite um número para multiplicar => "))

for y in range(len(vetor_M)):
    vetor_M[y] = multiplicador * vetor_A[y]

print(vetor_A)
print(multiplicador)
print(vetor_M)