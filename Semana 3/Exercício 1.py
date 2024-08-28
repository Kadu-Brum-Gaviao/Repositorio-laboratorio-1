hora = float(input('Digite a quantidade de horas trabalhadas: '))

salario = 35.00 * hora

if salario < 1000:
    salario = salario + 300
else:
    salario = 35.00 * hora

print('O salário total é:', salario)
