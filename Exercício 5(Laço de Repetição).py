maiorIdade = 0
menorIdade = 999
totalSalarios = 0
somaSalario = 0
contadorMulheres = 0

for i in range(10):
    idade = int(input('Cadastre uma idade: '))
    sexo = input('Cadastre um sexo (M/F): ').upper()
    salario = float(input('Informe o salário: '))
    somaSalario += salario
    totalSalarios += 1
    if idade > maiorIdade:
        maiorIdade = idade
    if idade < menorIdade:
        menorIdade = idade
    if sexo == 'F' and salario <= 10000:
        contadorMulheres += 1


mediaSalario = somaSalario / totalSalarios

print(f'A média salarial do grupo é: {mediaSalario:.2f}')
print(f'A maior idade do grupo é: {maiorIdade}')
print(f'A menor idade do grupo é: {menorIdade}')
print(f'A quantidade de mulheres com salário até R$10000,00 é: {contadorMulheres}')
