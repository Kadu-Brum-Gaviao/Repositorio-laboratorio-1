def valores():
    lista = []
    return lista

def acrescentarValores(lista):
    while len(lista) < 10: 
        numeros  = int(input('Digite um valor: '))
        lista.append(numeros)
    return lista, numeros

def maior(lista, numeros):
    maiores = 0
    if numeros > 100:
        i += 1
    return lista, maiores


def main(lista, maiores):
    print(f'Lista: {lista}')
    print(f'Valores maior que 10: {maiores}')
