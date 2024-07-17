time_1 = input('Nome do Primeiro Time: ')
time_2 = input('Nome do Segundo Time: ')
gols_1 = int(input('Quantidade de Gols do primeiro time: '))
gols_2 = int(input('Quantidade de Gols do Segundo time: '))

if gols_1 == gols_2:
    print("Empatado")
elif gols_1 > gols_2:
    print(f'{time_1} Venceu')
else:
    print(f'{time_2} Venceu')
    print('Time {}'.format(time_2))