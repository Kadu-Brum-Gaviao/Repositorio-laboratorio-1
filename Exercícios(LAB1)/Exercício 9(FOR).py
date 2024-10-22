santaMariaA = 0
santaMariaB = 0
santaMariaC = 0
totalPessoas = 20
opcao = ""

for i in range(totalPessoas):
    opcao = input('Escolha um dos jornais (A/B/C): ').upper()
    while (opcao != 'A') and (opcao != 'B') and (opcao != 'C'):
        print('Erro. Tente novamente...')
        opcao = input('Escolha um dos jornais (A/B/C): ').upper()
    if opcao == 'A':
        santaMariaA += 1
    elif opcao == 'B':
        santaMariaB += 1
    elif opcao == 'C':
        santaMariaC += 1

porcentagemA = (santaMariaA / totalPessoas) * 100
porcentagemB = (santaMariaB / totalPessoas) * 100
porcentagemC = (santaMariaC / totalPessoas) * 100

if porcentagemA > porcentagemB and porcentagemA > porcentagemC:
    print('Porcentagem do jornal (Santa Maria A): ', porcentagemA)
    if porcentagemB > porcentagemC:
        print('Porcentagem do jornal (Santa Maria B): ', porcentagemB)
        print('Porcentagem do jornal (Santa Maria C): ', porcentagemC)
    elif porcentagemC > porcentagemB:
        print('Porcentagem do jornal (Santa Maria C): ', porcentagemC)
        print('Porcentagem do jornal (Santa Maria B): ', porcentagemB)
elif porcentagemB > porcentagemA and porcentagemB > porcentagemC:
    print('Porcentagem do jornal (Santa Maria B): ', porcentagemB)
    if porcentagemA > porcentagemC:
        print('Porcentagem do jornal (Santa Maria A): ', porcentagemA)
        print('Porcentagem do jornal (Santa Maria C): ', porcentagemC)
    elif porcentagemC > porcentagemA:
        print('Porcentagem do jornal (Santa Maria C): ', porcentagemC)
        print('Porcentagem do jornal (Santa Maria A): ', porcentagemA)
elif porcentagemC > porcentagemA and porcentagemC > porcentagemB:
    print('Porcentagem do jornal (Santa Maria C): ', porcentagemC)
    if porcentagemA > porcentagemB:
        print('Porcentagem do jornal (Santa Maria A): ', porcentagemA)
        print('Porcentagem do jornal (Santa Maria B): ', porcentagemB)
    elif porcentagemB > porcentagemA:
        print('Porcentagem do jornal (Santa Maria B): ', porcentagemB)
        print('Porcentagem do jornal (Santa Maria A): ', porcentagemA)
