"""
Faça um algoritmo que leia dois valores e apresente:
O maior deles
O menor deles

Obs. o algoritmo deve verificar se os valores digitados são iguais.
"""

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O maior número é {num1}! O menor é {num2}!')
elif num2 > num1:
    print(f'O maior número é {num2}! O menor é {num1}!')
else:
    print('Os dois valores são iguais!')
