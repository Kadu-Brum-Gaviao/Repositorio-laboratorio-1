opcao = 0

while opcao != 5:
    print('\nMenu:')
    print('1. Idade')
    print('2. Salário')
    print('3. Sexo (f/m)')
    print('4. Estado Civil (s, c, v, d)')
    print('5. Sair')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        idade = int(input('Cadastre uma idade (entre 0 e 150): '))
        while idade < 0 or idade > 150:
            print('Idade Inválida. Tente novamente.')
            idade = int(input('Cadastre uma idade (entre 0 e 150): '))
        print(f'Idade Validada: {idade}')

    elif opcao == 2:
        salario = float(input('Cadastre um salário (maior que zero): '))
        while salario <= 0:
            print('Cadastro de salário inválido. Tente novamente.')
            salario = float(input('Cadastre um salário (maior que zero): '))
        print(f'Cadastro de salário validado: {salario}')

    elif opcao == 3:
        sexo = input('Digite seu sexo (f/m): ').lower()
        while sexo not in ['f', 'm']:
            print('Informação Inválida. Tente novamente.')
            sexo = input('Digite seu sexo (f/m): ').lower()
        print(f'Informação Válida: {sexo}')

    elif opcao == 4:
        estadoCivil = input('Cadastre o estado civil (s, c, v, d): ')
        while estadoCivil not in ['s', 'c', 'v', 'd']:
            print('Informação Inválida. Tente novamente.')
            estadoCivil = input('Cadastre o estado civil (s, c, v, d): ')
        print(f'Informação Válida: {estadoCivil}')

    elif opcao == 5:
        print('Saindo...')

    else:
        print('Opção Inválida. Digite outra opção.')
