opcao = 0
saldoAtual = float(input('Seu saldo atual é: '))

while opcao != 4:
    print('1 - Sacar')
    print('2 - Depositar')
    print('3 - Saldo')
    print('4 - Sair do programa')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        saque = float(input('Quanto dinheiro você quer sacar: '))
        if (saldoAtual >= saque) and (saque > 0):
            saldoAtual = saldoAtual - saque
            print(f'Você sacou: R${saque}')
        else:
            print('Saque invalido')
    elif opcao == 2:
        deposito = float(input('Você quer depositar quanto dinheiro: R$'))
        if deposito > 0:
            saldoAtual = saldoAtual + deposito
            print(f'Você depositou: R${deposito:.2f}')
        else:
            print('Deposito invalido')
    elif opcao == 3:
        print(f'Seu saldo atual é: {saldoAtual:.2f}')
    elif opcao == 4:
        print('Saindo do programa...')
    else:
        print('Opção invalida...')
