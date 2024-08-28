altura = float(input('Digite sua altura: '))

sexo = input('Digite seu sexo: ')

if sexo == 'Homem':
    pesoIdeal = (72.7 * altura) - 58
    print(f'O peso ideal do homem é: {pesoIdeal:.2f} ')
else:
    pesoIdeal = (62.1 * altura) - 44.7
    print(f'O peso ideal da mulher é: {pesoIdeal:.2f} ')
