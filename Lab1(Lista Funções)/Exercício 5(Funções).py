def menu():
    print('1. Sacar')
    print('2. Depositar')
    print('3. Saldo')
    print('4. Sair')
    opc = int(input('Selecione uma opção: '))
    return opc

def mostrar_saldo(saldo):
    print(f'Seu saldo é: {saldo}')

def saque(saldo):
    sacar = float(input('Quanto você deseja sacar: '))
    if sacar <= saldo:
        saldo -= sacar
        print(f'Você sacou R${sacar}')
    else:
        print('Saldo Insuficiente')
    print(f'Seu saldo atual é: {saldo}')
    return saldo
    

def deposito(saldo):
    depositar = float(input('Quanto você deseja depositar: '))
    while depositar <= 0:
        print('Deposito inválido. Tente novamente.')
        depositar = float(input('Quanto você deseja depositar: '))
    saldo += depositar
    print(f'Você depositou R${depositar}')
    print(f'Seu saldo atual é: {saldo}')
    return saldo

def main():
    saldo = 0
    while True:
        opc = menu()

        if opc == 1:
            saldo = saque(saldo)
        elif opc == 2:
            saldo = deposito(saldo)
        elif opc == 3:
            mostrar_saldo(saldo)
        elif opc == 4:
            print('Saindo do sistema.')
            break
        else:
            print('Opção Inválida. Tente novamente.')

main()
