hora_1 = int(input('Digite a Hora 1: '))
minutos_1 = int(input('Digite os Minutos 1: '))

hora_2 = int(input('Digite a Hora 2: '))
minutos_2 = int(input('Digite os Minutos 2: '))

hora = hora_1 + hora_2
minutos = minutos_1 + minutos_2

if hora > 12:
    hora = hora - 12
    hora += 1

if hora > 12:
    hora = hora - 12
    hora += 1

if minutos >= 60:
    minutos = minutos - 60

print(hora,':',minutos)