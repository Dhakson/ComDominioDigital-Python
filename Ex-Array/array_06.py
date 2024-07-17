nomes = ["",""]
senhas = [0,0]

while True:
    print("[1] - Cadastrar \n[2] - Login ")
    opcao = int(input("Escolha a opção: "))
    if opcao == 1:
        for c in range(2):
            nomes[c] = input("Crie um Login: ")
            senhas[c] = int(input("Crie uma Senha: "))
            print("Usuario Cadastrado com Sucesso!")
            print(nomes,senhas)
    elif opcao == 2:
        nome = input("Login: ")
        senha = int(input("Senha: "))
        for x in range(2):
            if nome != nomes[x] and senha != senhas[x]:
                print("Usuario não Encontrado")

            else:
                if nome == nomes[x] and senha == senhas[x]:
                    print("Logando...")