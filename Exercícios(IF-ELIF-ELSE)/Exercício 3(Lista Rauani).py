num = float(input('Digite um número: '))

if (num % 2 == 0) and (num % 3 == 0):
    print('O número é divisivel por 2 e 3.')
elif num % 2 == 0:
    print('O número é divisivel por 2.')
elif num % 3 == 0:
    print('O número é divisivel por 3.')
else:
    print('O número não é divisivel por 3 ou 5.')