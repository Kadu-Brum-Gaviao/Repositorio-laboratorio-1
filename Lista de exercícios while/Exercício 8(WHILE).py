somaIdade = 0
numPessoas = 15
contagemIdadesValidas = 0  

# Loop para coletar idades
for i in range(numPessoas):
    idade = int(input('Cadastre uma idade: '))
    if idade < 0 or idade > 150:
        print('Idade inválida. Insira uma idade entre 0 e 150.')
        continue
    somaIdade += idade
    contagemIdadesValidas += 1

if contagemIdadesValidas > 0:
    media = somaIdade / contagemIdadesValidas

    # Verificação da categoria de idade
    if media > 0 and media <= 25:
        categoriaIdade = 'Jovem'
    elif media >= 26 and media <= 60:
        categoriaIdade = 'Adulto'
    else:
        categoriaIdade = 'Idoso'

    print(f'A média da idade é: {media:.2f}')
    print(f'A média da turma se encontra na categoria: {categoriaIdade}')
else:
    print('Nenhuma idade válida foi cadastrada.')