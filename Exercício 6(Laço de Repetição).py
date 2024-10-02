maiorIdade = 0

for i in range(10):
    idade = int(input('Cadastre uma idade: '))
    if idade >= 18:
        maiorIdade += 1

print(f'Quantidade de pessoas com 18 anos ou mais: {maiorIdade}')
