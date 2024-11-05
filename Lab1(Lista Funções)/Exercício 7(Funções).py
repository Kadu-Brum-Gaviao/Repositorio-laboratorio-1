def horario():
    horas = int(input('Que horas são(0 a 23): '))
    minutos = int(input('Qual a minutagem:(0 a 59): '))
    return horas, minutos

def main():
    horas, minutos = horario()

    if horas == 0:
        print(f'Horas: 12:{minutos:02d} AM')
    elif horas < 12:
        print(f'Horas: {horas:02d}:{minutos:02d} PM')
    else:
        horas -= 12
        print(f'Horas: {horas:02d}:{minutos:02d} PM')


main()