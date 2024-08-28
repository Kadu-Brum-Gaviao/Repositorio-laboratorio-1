precoLitro = float(input('Digite o preço da gasolina: '))

precoPagar = float(input('Digite a quantia de dinheiro gasta: '))

quantidadeLitros = precoPagar / precoLitro
print("A quantidade de litros é:", quantidadeLitros)

precoTotal = precoLitro * quantidadeLitros
print('O preço total da gasolina é: ', precoTotal)
