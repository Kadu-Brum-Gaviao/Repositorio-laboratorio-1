categoria = input('Digite sua categoria: ').upper()
valorCompra = float(input('Digite o valor total da compra: '))
percentual = 0

if categoria == 'REGULAR':
    if valorCompra > 100:
        percentual = 0.05
elif categoria == 'VIP':
    if valorCompra > 500:
        percentual = 0.20
    elif valorCompra > 100:
        percentual = 0.10
elif categoria == 'PLATINUM':
    if valorCompra > 500:
        percentual = 0.25
    elif valorCompra > 100:
        percentual = 0.15
valorDesconto = valorCompra * percentual
valorFinal = valorCompra - valorDesconto

print(f'Você recebeu R${valorDesconto} de desconto, valor final = {valorFinal}')
