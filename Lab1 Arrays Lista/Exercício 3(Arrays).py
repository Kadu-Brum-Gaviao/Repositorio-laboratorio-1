def valores():
    lista = []
    return lista

def acrescentarValores(lista):
    while len(lista) < 10:
        numeros = int(input('Digite um valor: '))

        if numeros not in lista:
            lista.append(numeros)
        else:
            print(f'{numeros} já está na lista. Tente novamente.')
    
    return lista

def valoresPares(lista):
    pares = []
    posicoes = []
    for i in  range(len(lista)):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
            posicoes.append(i)
    return pares, posicoes



def main():
    lista = valores()
    lista = acrescentarValores(lista)
    pares, posicoes = valoresPares(lista)
    print(f'Lista: {lista}')
    print(f'Valores pares: {pares}')
    print(f'Posições dos valores pares: {posicoes}')

main()
