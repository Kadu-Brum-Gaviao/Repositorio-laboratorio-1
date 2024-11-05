def cinco_notas():
    somaNotas = 0
    for i in range(5):
        while True:
            notas = float(input('Registre uma nota: '))
            if notas < 0:
                print('Nota inválida. Insira um valor positivo.')
            else:
                somaNotas += notas
                break
    return somaNotas

def media(somaNotas):
    resultado = somaNotas / 5
    return resultado

def main():
    somaNotas = cinco_notas()
    resultado = media(somaNotas)

    if resultado < 4:
        print(f'Média = {resultado}: Reprovado')
    elif resultado >= 4 and resultado < 7:
        print(f'Média = {resultado}: Recuperação')
    else: 
        print(f'Média = {resultado}: Aprovado')


main()
