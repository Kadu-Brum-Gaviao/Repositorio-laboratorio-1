opcao = 0
contador = 0
somaAltura = 0
somaIdade = 0
mediaAltura = 0
mediaIdade = 0

while opcao != 3:
    print('1 - Cadastrar pessoa')
    print('2 - Mostrar média parcial de altura e idade')
    print('3 - Sair')
    opcao = int(input('Digite um número de 1 a 3: '))
    if opcao == 1:
        altura = float(input('Digite sua altura: '))
        idade = int(input('Digite sua idade: '))
        contador += 1
        somaAltura = somaAltura + altura
        somaIdade = somaIdade + idade
    elif opcao == 2:
        mediaAltura = somaAltura / contador
        mediaIdade = somaIdade / contador
        print(f'A média da altura é: {mediaAltura}')
        print(f'A média da idade é: {mediaIdade}')
    elif opcao == 3:
        mediaAltura = somaAltura / contador
        mediaIdade = somaIdade / contador
        print('Saindo do programa...')
        print(f'A média da altura é: {mediaAltura}')
        print(f'A média da idade é: {mediaIdade}')
    else:
        print('Opção Invalida...')
