def quantidade_laranjas():
    numLaranjas = int(input('Quantas laranjas você deseja comprar: '))
    return numLaranjas

def compra_laranjas(numLaranjas):
    if numLaranjas > 12:
        precoUnitario = 0.25
    else: 
        precoUnitario = 0.40
    return numLaranjas * precoUnitario

def main():
    numLaranjas = quantidade_laranjas()
    valorTotal = compra_laranjas(numLaranjas)
    print(f'O valor total da compra é: {valorTotal:.2f}')
  
main()
