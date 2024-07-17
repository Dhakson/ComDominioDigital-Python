def iterador_texto():
    frase = "O rato roeu a roupa do rei de Roma"
    qntd = qntd_espaco = vogal = 0
    for x in range(len(frase)):
        if frase[x] == " ":
            qntd_espaco +=1
        qntd += 1

    for z in frase:
        if z in "aeiouAEIOU":
            vogal += 1

    print(f"Quantidade de Vogais: {vogal}")
    print(f'Tamanho da Frase: {qntd}')
    print(f"Quantidade de Espaço: {qntd_espaco}")