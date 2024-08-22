import math
pi = math.pi

# Questão - Soma

numero1 = int(input("Digite se número aqui: "))
numero2 = int(input("Digite seu número aqui: "))

soma = numero1 + numero2

print("O resultado da soma é: ", soma)

# Questão - Dobro

dobro1 = numero1 * 2
dobro2 = numero2 * 2
dobro_final = numero1 + numero2 * 2

print("O dobro do primeiro número é: ", dobro1)
print("O dobro do segundo número é: ", dobro2)
print("O dobro da soma dos números é: ", dobro_final)

# Questão - Divisão

divisao1 = numero1 / numero2
divisao2 = numero2 / numero1

print("A divisão do primeiro número pelo segundo é: ", divisao1)
print("A divisão do segundo número pelo primeiro é: ", divisao2)

# Questão - Subtração

subtracao = numero1 - numero2

# Questão - Área do Circulo

print("O resultado da subtração é: ", subtracao)

print("O valor de pi é: ", pi)

valor_do_raio = int(input("Digite o valor do raio: "))
area_do_circulo = math.pi * valor_do_raio ** 2

print("A área do circulo é: ", area_do_circulo)

# Questão - Quantidade de Combustivel

distancia_total_km = float(input("Digite a distância percorrida(Quilometros): "))
quantidade_de_combustivel = float(input("Digite a quantidade de combustivel consumida(Litros): "))

if quantidade_de_combustivel == 0:
    print("A quantidade de combustivel não pode ser zero.")

consumo_medio_combustivel = distancia_total_km / quantidade_de_combustivel

print("O Consumo Médio é: ", consumo_medio_combustivel)

# Questão - Média do Aluno

nome = input("Digite o nome do aluno: ")

media1 = float(input("Digite o valor da primeira média: "))
media2 = float(input("Digite o valor da segunda média: "))
media3 = float(input("Digite o valor da terceira média: "))
media_do_aluno = (media1 + media2 + media3) / 3

print("A média final é: ", media_do_aluno)

print(f"\nNome do aluno: {nome}")
print(f"Média do Aluno: {media_do_aluno}")

# Questão - Fahrenheit pra Celsius

graus_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

graus_celsius = (graus_fahrenheit - 32) * 5 / 9
print("A temperatura em graus celsius é: ", graus_celsius)

# Questão - Preço Total(Melão)

melao = 4.25

quantidade_desejada_melao = int(input("Digite a quantidade de melões desejados: "))

preco_total = melao * quantidade_desejada_melao
print("O preço total de todos os melões é: ", preco_total)

# Questão - Aumento de Preço

produto = input("Digite o nome do produto: ")

preco_do_produto = float(input("Digite o preço do produto: "))

aumento_de_preco = 0.65
preco_total_venda = preco_do_produto * (1 + aumento_de_preco)

print("O valor total do produto é: ", preco_total_venda)
