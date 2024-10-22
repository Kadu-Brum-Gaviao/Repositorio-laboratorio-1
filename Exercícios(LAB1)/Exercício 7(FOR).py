num1 = int(input('Digite um número (menor): '))
num2 = int(input('Digite um número (maior): '))

while num1 >= num2:
    print('Erro. O primeiro número deve ser menor que o segundo. Tente Novamente.')
    num1 = int(input('Digite um número (menor): '))
    num2 = int(input('Digite um número (maior): '))

print(f'Números pares entre {num1} e {num2}:')
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(i)