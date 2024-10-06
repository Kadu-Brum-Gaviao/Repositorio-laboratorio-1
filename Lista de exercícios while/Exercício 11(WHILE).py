numAlunos = 25
idadeAlunos = []
somaIdade = 0

for i in range(numAlunos):
    idade = int(input('Cadastre uma idade: '))
    idadeAlunos.append(idade)
    somaIdade += idade

maiorIdade = max(idadeAlunos)
menorIdade = min(idadeAlunos)
media = somaIdade / numAlunos

print(f'A maior idade da lista de alunos é: {maiorIdade}')
print(f'A menor idade da lista de alunos é: {menorIdade}')
print(f'A média de idades é: {media}')