while True:
    somaProduto = 0
    numProduto = 1

    print('Lojas Tabajara')

    while True:
        produto = float(input('Custo do produto: '))
        if produto == 0:
            break
        elif produto < 0:
            print('Preço invalido, tente novamente...')
            continue
        somaProduto += produto
        numProduto += 1

    print(f'Total: R${somaProduto:.2f}')

    while True:
        dinheiroFornecido = float(input('Quanto dinheiro foi entregue ao caixa: '))
        if dinheiroFornecido < somaProduto:
            print('Erro na transação, valor fornecido é menor que o total...')
        else:
            troco = dinheiroFornecido - somaProduto
            print(f'Troco: R${troco:.2f}')
            break

    novaCompra = input('Deseja comprar algo mais? (s/n): ').lower()
    if novaCompra != 's':
        print('Comprar finalizadas.')
        break