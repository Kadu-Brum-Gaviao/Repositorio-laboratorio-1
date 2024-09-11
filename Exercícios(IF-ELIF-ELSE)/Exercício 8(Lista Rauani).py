peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)

if (imc < 18.5) and (imc > 0):
    print('Abaixo do peso.')
elif (imc >= 18.5) and (imc <= 24.9):
    print('Peso Normal.')
elif (imc >= 25) and (imc  <= 29.9):
    print('Sobrepeso.')
elif imc > 30:
    print('Obesidade.')
else:
    print('Erro no calcúlo!')
    
