def vetorA():
    listaA = []
    return listaA

def acrescentarValores(listaA):
    while len(listaA) < 10:
        num = int(input('Digite um valor: '))

        if num not in listaA:
            listaA.append(num)
        else: 
            print(f'{num} ja foi inserido na lista. Tente novamente')
    return listaA

def vetorB(listaA):
    listaB = []       

    for i in range(len(listaA) -1, -1, -1):
        listaB.append(listaA[i])
    return listaB

def main():
    listaA = vetorA()
    listaA = acrescentarValores(listaA)
    listaB = vetorB(listaA)
    print(f'Lista: {listaA}')
    print(f'Lista inversa: {listaB}')

main()
