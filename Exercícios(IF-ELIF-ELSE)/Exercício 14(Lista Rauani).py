horaAtual = float(input('Que horas são: '))

if (horaAtual < 0) or (horaAtual > 24):
    print('Horário Inválido')
elif (horaAtual > 6) and (horaAtual < 18):
    print('Período Diurno')
else:
    print('Período Noturno')
