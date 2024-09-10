"""
Faça um algoritmo que apresente qual veículo o usuário pode dirigir.
Com isso, solicite o tipo da carteira de motorista e apresente:

"""

print('Qual categoria de veiculo você pode utilizar?')
print("A. Motos e triciclos.")
print("B. Carros de passeio.")
print("C. Veiculos de carga acima de 3,5 toneladas.")
print("D. Veiculos com mais de 8 passageiros.")
print("E. Veiculos com unidade acoplada acima de 6 toneladas.")

veiculo = input('Seu veiculo esta dentro da categoria: ').upper()

if veiculo == 'A':
    print(f'Você possui uma carteira de motorista de categoria A!')
    print(f'Você pode pilotar motos e triciclos!')
elif veiculo == 'B':
    print(f'Você possui uma carteira de motorista de categoria B!')
    print(f'Você pode pilotar carros de passeio!')
elif veiculo == 'C':
    print(f'Você possui uma carteira de motorista de categoria C!')
    print(f'Você pode pilotar veiculos de carga acima de 3,5 toneladas!')
elif veiculo == 'D':
    print('Você possui uma carteira de motorista de categoria D!')
    print(f'Você pode pilotar veiculos com mais de 8 passageiros!')
elif veiculo == 'E':
    print(f'Você possui uma carteira de motorista de categoria E!')
    print(f'Você pode pilotar veiculos com unidade acoplada acima de 6 toneladas.')
else:
    print(f'Opção invalida!')
