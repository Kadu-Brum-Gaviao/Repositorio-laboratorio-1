def Criarlista():
    listaInicial = []
    return listaInicial 

def acrescentarLista(lista):
    i = 0
    somaNumeros = 0
    somaTotal = 0
    while len(lista) < 8:
        numeros = int(input('Digite os números: '))

        if numeros > 30:
            somaNumeros += numeros
            i += 1  
        somaTotal += numeros
        lista.append(numeros)
    print(lista)
    print(f'Números maiores que 30: {i}')
    print(f'Soma dos números maiores que 30: {somaNumeros}')
    print(f'Soma de todos os números: {somaTotal}')

def main(): 
    lista = Criarlista()
    acrescentarLista(lista)

main()
