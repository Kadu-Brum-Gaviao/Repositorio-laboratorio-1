"""
def calcular_media(v1, v2):
    media = (v1 + v2) / 2
    return media

def main():
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))

    mediaFora = calcular_media(valor1, valor2)
    print('média: ', mediaFora)

main()
"""
def menu():
    print('1. Sacar')
    print('2. Depositar')
    print('3. Saldo')
    print('4. Sair')
    opcao = int(input('Selecione uma opção: '))
    return opcao

def mostrar_saldo(saldo):
    print('Seu saldo é: ', saldo)

def sacar(saldo):
    valorSaque = float(input('Digite o valor: '))
    if valorSaque <= saldo:
        saldo = saldo - valorSaque
        mostrar_saldo(saldo)
    else: 
        print('Saldo inficiente.')
    return saldo

def depositar(saldo):
    valor = float(input('Digite valor: '))
    saldo = saldo + valor
    mostrar_saldo(saldo)
    return saldo

def main():
    opcao = 0
    saldo = 0 

    while opcao != 4: 
        opcao = menu()
        
        if opcao == 1:
            saldo = sacar(saldo)
        elif opcao == 2:
            saldo = depositar(saldo)
        elif opcao == 3:
            mostrar_saldo(saldo)




main()