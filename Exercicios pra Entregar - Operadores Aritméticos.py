quantidade_de_cavalos = int(input("Digite a quantidade de cavalos: "))
ferraduras_por_cavalo = 4

preco_ferradura = 80.00

valor_total_ferraduras = preco_ferradura * quantidade_de_cavalos * ferraduras_por_cavalo
print("Valor total das ferraduras: ", valor_total_ferraduras)

# Questão 1

preco_da_roupa = float(input("Digite o custo da peça de roupa: "))

aumento_do_preco = 0.30
preco_total_roupa = preco_da_roupa * (1 + aumento_do_preco)

print("O custo total da peça de roupa é: ", preco_total_roupa)

# Questão 2

numero = float(input("Digite o número: "))

metade_do_numero = numero / 2
dobro_do_numero = numero * 2

print("A metado do número é: ", metade_do_numero)
print("O dobro do número é: ", dobro_do_numero)

# Questão 3

ano_de_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = 2024
idade = ano_atual - ano_de_nascimento

print("A sua idade é: ", idade)

# Questão 4

total_de_carros = int(input("Digite a quantidade de carros: "))
quantidade_de_pneus_por_carro = 4
preco_do_pneu = 395.40

valor_total_pneus = total_de_carros * quantidade_de_pneus_por_carro * preco_do_pneu
print("O total do valor dos pneus é: ", valor_total_pneus)
