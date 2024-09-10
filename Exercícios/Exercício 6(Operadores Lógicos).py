"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                              Até 5 Kg                 Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã              R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

"""

morangoPorQuiloAte5Kg = 2.50
morangoPorQuiloAcima5Kg = 2.20
macaPorQuiloAte5Kg = 1.80
macaPorQuiloAcima5Kg = 1.50

quantidadeQuiloMorango = float(input('Quantos quilos de morango foram comprados: '))
quantidadeQuiloMaca = float(input('Quantos quilos de maçã foram comprados: '))

if quantidadeQuiloMorango < 0 or quantidadeQuiloMaca < 0:
    print('É impossível fazer essa transação!')

if quantidadeQuiloMorango > 5:
    precoTotalMorango = morangoPorQuiloAcima5Kg * quantidadeQuiloMorango
else:
    precoTotalMorango = morangoPorQuiloAte5Kg * quantidadeQuiloMorango

if quantidadeQuiloMaca > 5:
    precoTotalMaca = macaPorQuiloAcima5Kg * quantidadeQuiloMaca
else:
    precoTotalMaca = macaPorQuiloAte5Kg * quantidadeQuiloMaca

precoTotalFrutas = precoTotalMorango + precoTotalMaca

if (quantidadeQuiloMorango + quantidadeQuiloMaca > 8) or (precoTotalFrutas > 25):
    precoTotalFrutas *= 0.90

print(f'O preço total das frutas é: R${precoTotalFrutas:.2f}')
