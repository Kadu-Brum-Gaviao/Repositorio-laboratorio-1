num = 1
contador = 0

while num != 0:
    num = int(input('Digite um número: '))
    if num == 10:
        contador += 1
    elif num == 0:
        print('Saindo do Programa')
print(f'O número 10 foi escolhido: {contador} vezes.')


