grausCelsius = float(input('Digite a temperatura: '))

if grausCelsius < 10:
    print('Frio')
elif grausCelsius >= 10 and grausCelsius <= 25:
    print('Agradável')
else:
    print('Quente')