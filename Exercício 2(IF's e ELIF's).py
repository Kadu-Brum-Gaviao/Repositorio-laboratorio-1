"""
Um sistema de uma loja de roupas permite que as peças de
roupas sejam vendidas de três formas diferentes:
À vista.
2 vezes.
3 vezes.
Para isso, o sistema deve ler o valor da peça, a opção de pagamento
e apresentar o valor das parcelas.
"""

print("Escolha a forma de pagamento: ")
print("1. À vista.")
print("2. Duas vezes.")
print("3. Três vezes.")

opcao = int(input('Digite a opção escolhida: '))
preco = float(input('Informe o preço da peça de roupa: '))

if opcao == 1:
    valor = preco
    print(f'Compra concluida. Preço do produto: R${valor:.2f}!')
elif opcao == 2:
    valor = preco / 2
    print(f'Compra concluida. Preço do produto: R${valor:.2f}!')
    print(f'O valor é duas vezes de R${valor:.2f}!')
elif opcao == 3:
    valor = preco / 3
    print(f'Compra concluida. Preço do produto: R${valor:.2f}!')
    print(f'O valor é três vezes de R${valor:.2f}!')
else:
    print('Opção de pagamento invalida!')
