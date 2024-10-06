import random
numeroSorteio = random.randint(1, 100)
num = 0

while numeroSorteio != num:
    num = int(input('Digite um número: '))
    if num < 1 or num > 100:
        print('Número invalido, tente novamente...')
    elif num > numeroSorteio:
        print('Tente um número menor...')
    elif num < numeroSorteio:
        print('Tente um número maior...')

print('Parabens, você acertou o número!')
