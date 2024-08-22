# Desconto no preço

valor_produto = float(input("Digite o valor do produto: "))
reducao_do_preco = 0.80

valor_final = valor_produto * reducao_do_preco
print("O valor final é: ", valor_final)

# Bicicleta

populacao = int(input("Digite a população do Recanto Maestro: "))
numero_bicicletas = int(input("Digite quantas pessoas andam de bicicleta: "))

total_de_pessoas_porcentagem = 100

pessoas_que_andam_de_bicicleta = (numero_bicicletas * total_de_pessoas_porcentagem) / populacao

print("A porcentagem total de é: ", pessoas_que_andam_de_bicicleta)

# Filtro de Ar

preco_por_unidade_filtro = float(input("Digite o preço por unidade dos filtros de ar: "))
numero_de_caixas_filtros_total = int(input("Digite a quantidade de caixas que contenham filtros: "))
filtros_por_caixa = 4

valor_inicial = preco_por_unidade_filtro * numero_de_caixas_filtros_total * filtros_por_caixa

impostos = 1.14
valor_final_1 = (preco_por_unidade_filtro * impostos) * 1.35

valor_final_2 = valor_final * numero_de_caixas_filtros_total * filtros_por_caixa

lucro = valor_final - valor_inicial
print("Valor da Compra: ", valor_inicial)
print("Valor da Venda: ", valor_final_2)
print("Lucro: ", lucro)
