"""
Crie um programa que leia o nome, o salário e o tempo de serviço de
um funcionário e informe se ele tem direito a receber um aumento. O
funcionário deve ter pelo menos 5 anos de serviço e o salário não pode
ser superior a R$ 2.000,00 para receber o aumento de 10%. Caso
contrário, o aumento é de 5%.

"""

nome = input("Digite o nome do funcionário: ")
tempoDeServiço = int(input("Tempo de serviço do funcionário(em anos): "))
salarioMensal = float(input("Salário de um mês de trabalho: "))

if (tempoDeServiço >= 5) and (salarioMensal <= 2000 and salarioMensal > 0):
    percentual = 10
elif (tempoDeServiço < 5) or (salarioMensal > 2000 and salarioMensal > 0):
    percentual = 5
else:
    print('Opção Invalida...')

percentual = percentual / 100.00
aumento = percentual * salarioMensal
salarioFinal = salarioMensal + aumento

print(f'O salário com aumento é: {salarioFinal}!')
