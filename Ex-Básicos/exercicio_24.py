senha_secreta = 1234

#senha = int(input('Digite a senha: '))

qntd = 0

tentativa = 3

while qntd < tentativa:
    senha = int(input('Digite a sua senha: '))
    if senha != senha_secreta:
        #senha = int(input('Senha Incorreta. Digite novamente: '))
        print("Senha Incorreta!")
        qntd += 1
    else:
        print('Seja Bem vindo')
        break

    if qntd >= 3:
        print('Cont Bloqueada')
        break