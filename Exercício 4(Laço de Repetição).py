"""
Faça um programa que receba a idade e o peso de 7 pessoas, calcule e mostre:
A média das idades das 7 pessoas;
Quantidade de pessoas maiores de idade.
Porcentagem de pessoas com idade entre 10 e 30 anos
"""
contador = 0
somaIdade = 0
maiorIdade = 0
pessoas_10_a_30 = 0

for i in range(7):
    idade = int(input(f'Cadastre a idade da {i + 1}ª pessoa: '))
    peso = float(input(f'Cadastre o peso da {i + 1}ª pessoa:'))
    somaIdade += idade
    if idade >= 18:
        maiorIdade += 1
    if 10 <= idade <= 30:
        pessoas_10_a_30 += 1

mediaIdade = somaIdade / 7

porcentagem10a30 = (pessoas_10_a_30 / 7) * 100

print(f'A média de idades é {mediaIdade:.2f}')
print(f'Quantidade de pessoas maiores de idade: {maiorIdade}')
print(f'Porcentagem de pessoas com idade entre 10 e 30 anos: {porcentagem10a30:.2f}%')
