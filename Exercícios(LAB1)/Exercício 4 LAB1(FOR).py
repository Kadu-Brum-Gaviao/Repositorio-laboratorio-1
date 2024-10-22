quantidadePares = 0
quantidadeImpares = 0
quantidadeZeros = 0

for i in range(10):
    try:
        numero = int(input('Digite um número: '))
        
        if numero == 0:
            quantidadeZeros += 1
        elif numero % 2 == 0:
            quantidadePares += 1
        else:
            quantidadeImpares += 1
    except ValueError:
        print('Valor inválido, tente novamente.')

print(f'Quantidade de números pares: {quantidadePares}')
print(f'Quantidade de números ímpares: {quantidadeImpares}')
print(f'Quantidade de zeros: {quantidadeZeros}')
