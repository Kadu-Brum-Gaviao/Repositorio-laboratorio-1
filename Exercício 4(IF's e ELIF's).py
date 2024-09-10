"""
Faça um algoritmo que leia dois valores. Posteriormente leia uma opção do menu:
1.Somar os dois valores.
2.Subtrair os dois valores.
3.Multiplicar os dois valores.
4.Dividir os dois valores
"""

print("Escolha uma das seguintes opções: ")
print("1. Somar os dois valores.")
print("2. Subtrair os dois valores.")
print("3. Multiplicar os dois valores.")
print("4. Dividir os dois valores.")

opcao = int(input('Escolha uma das seguintes opções: '))
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if opcao == 1:
    soma = num1 + num2
    print(f'O resultado da soma é: {soma:.2f}!')
elif opcao == 2:
    subtracao = num1 - num2
    print(f'O resultado da subtração é: {subtracao:2.f}!')
elif opcao == 3:
    multiplicacao = num1 * num2
    print(f'O resultado da multiplicação é: {multiplicacao:.2f}!')
elif opcao == 4:
    divisao = num1 / num2
    print(f'O resultado da divisão é: {divisao:.2f}!')
else:
    print('Opção Invalida!')
