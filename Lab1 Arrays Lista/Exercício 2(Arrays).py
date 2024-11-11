def valores():
    lista = []
    return lista

def acrescentarValores(lista):
    while len(lista) < 10: 
        numeros  = int(input('Digite um valor: '))
        lista.append(numeros)
    return lista

def maior(lista):
    maiores = []
    for numeros in lista:
        if numeros > 100:
            maiores.append(numeros)
    return maiores


def main():
    lista = valores()
    lista = acrescentarValores()
    maiores = maior(lista)
    print(f'Lista: {lista}')
    print(f'Valores maior que 100: {maiores}')

main()
