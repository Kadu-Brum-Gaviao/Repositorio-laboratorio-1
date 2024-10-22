totalPessoas = 15
sexoMasculino = 0
sexoFeminino = 0
olhosAzuis = 0
olhosVerdes = 0
olhosCastanhos = 0
cabelosLoiros = 0
cabelosCastanhos = 0
cabelosPretos = 0
listaIdade = []
mulheresVL = 0

for i in range(totalPessoas):
    print('a. Sexo: M(Masculino) e F(Feminino)')
    print('b. Cor dos olhos: A(azuis), V(verdes) e C(castanhos)')
    print('c. Cor dos cabelos: L(loiros), C(castanhos) e P(pretos)')
    print('d. Idade')
    
    sexo = ''
    while sexo not in ['M', 'F']:
        sexo = input('Registre o sexo de uma pessoa (M/F): ').upper()
        if sexo not in ['M', 'F']:
            print('Erro. Tente novamente.')

    if sexo == 'M':
        sexoMasculino += 1
    else:
        sexoFeminino += 1

    corOlhos = ''
    while corOlhos not in ['A', 'V', 'C']:
        corOlhos = input('Registre a cor dos olhos de uma pessoa (A/V/C): ').upper()
        if corOlhos not in ['A', 'V', 'C']:
            print('Erro. Tente novamente.')

    if corOlhos == 'A':
        olhosAzuis += 1
    elif corOlhos == 'V':
        olhosVerdes += 1
    else:
        olhosCastanhos += 1

    corCabelo = ''
    while corCabelo not in ['L', 'C', 'P']:
        corCabelo = input('Registre a cor do cabelo de uma pessoa (L/C/P): ').upper()
        if corCabelo not in ['L', 'C', 'P']:
            print('Erro. Tente novamente.')

    if corCabelo == 'L':
        cabelosLoiros += 1
    elif corCabelo == 'C':
        cabelosCastanhos += 1
    else:
        cabelosPretos += 1

    idade = int(input('Registre a idade de uma pessoa: '))
    listaIdade.append(idade)

    if sexo == 'F' and 18 <= idade <= 35 and corOlhos == 'V' and corCabelo == 'L':
        mulheresVL += 1

maiorIdade = max(listaIdade)
print(f'A maior idade desse grupo é: {maiorIdade}')

porcentagemOlhosAzuis = (olhosAzuis / totalPessoas) * 100
porcentagemOlhosVerdes = (olhosVerdes / totalPessoas) * 100
porcentagemOlhosCastanhos = (olhosCastanhos / totalPessoas) * 100

print(f'Porcentagem de pessoas com olhos azuis: {porcentagemOlhosAzuis:.2f}%')
print(f'Porcentagem de pessoas com olhos verdes: {porcentagemOlhosVerdes:.2f}%')
print(f'Porcentagem de pessoas com olhos castanhos: {porcentagemOlhosCastanhos:.2f}%')

porcentagemCabelosLoiros = (cabelosLoiros / totalPessoas) * 100
porcentagemCabelosCastanhos = (cabelosCastanhos / totalPessoas) * 100
porcentagemCabelosPretos = (cabelosPretos / totalPessoas) * 100

print(f'Porcentagem de pessoas com cabelos loiros: {porcentagemCabelosLoiros:.2f}%')
print(f'Porcentagem de pessoas com cabelos castanhos: {porcentagemCabelosCastanhos:.2f}%')
print(f'Porcentagem de pessoas com cabelos pretos: {porcentagemCabelosPretos:.2f}%')

porcentagemHomens = (sexoMasculino / totalPessoas) * 100
porcentagemMulheres = (sexoFeminino / totalPessoas) * 100

print(f'Porcentagem de pessoas do sexo masculino: {porcentagemHomens:.2f}%')
print(f'Porcentagem de pessoas do sexo feminino: {porcentagemMulheres:.2f}%')