def somaImposto(taxaImposto, custo):
    custoFinal = custo + (custo * (taxaImposto / 100))
    return custoFinal

def main():
    taxa = float(input('Taxa do produto: '))
    custo = float(input('Custo do produto: '))
    
    custoComImposto = somaImposto(taxa, custo)
    print(f'O custo final com imposto é: R$ {custoComImposto:.2f}')

main()
