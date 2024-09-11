num = float(input('Digite um número: '))

if (num % 3 == 0) and (num % 5 == 0):
    print(f'O número {num} é multiplo de 3 e 5.')
elif num % 3 == 0:
    print(f'O número {num} é multiplo de 3.')
elif num % 5 == 0:
    print(f'O número {num} é divisivel de 5')
else:
    print('O número não é multiplo de 3 ou 5.')