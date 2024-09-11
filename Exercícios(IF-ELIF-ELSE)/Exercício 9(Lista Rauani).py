num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
maior = num3

if (num1 > maior):
    maior = num1
if num2 > maior:
    maior = num2
print(f'O maior é {maior}!')
