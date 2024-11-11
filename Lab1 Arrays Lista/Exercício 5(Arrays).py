def menu():
    print('1 - Inserir item.')
    print('2 - Retirar item.')
    print('3 - Listar itens.')
    print('4 - Retirar todos os itens da lista.')
    print('5 - Sair')
    opc = int(input('Selecione uma opção: '))
    return opc

def  inserirItem(lista):
    item = input('Qual produto você deseja comprar: ')
    if item not in lista:
        lista.append(item)
        print(f'{item} adicionado(a) com sucesso.')
    else:
        print(f'Erro, {item} já foi adicionado(a). Tente novamente.')
    return lista

def retirarItem(lista):
    if len(lista) == 0:
        print('Nenhum elemento presente na lista. Adicione algum item.')
    else:
        try:
            index = int(input('Digite o indice do item que deseja remover 0 a {}: '.format(len(lista) - 1)))

            if index >= 0 and index < len(lista):
                removerItem = lista.pop(index)
                print(f'O item "{removerItem}" removido com sucesso')
            else:
                print('Indice invalido. Tente novamente.')
        except:
            print('Insira um número valido.')
    return lista

def listarItens(lista):
    if len(lista) > 0:
        print(f'Itens na lista: {lista}')
    else:
        print('Por favor. Adicione itens na lista.')

def removerTudo(lista):
    print(f'Itens: {lista} foram removidos.')
    while len(lista) > 0:
        lista.pop()
    return lista

def main():
    opcao = 0
    lista = []

    while opcao != 5:
        opcao = menu()
        if opcao == 1:
            inserirItem(lista)
        elif opcao == 2:
            retirarItem(lista)
        elif opcao == 3:
            listarItens(lista)
        elif opcao == 4:
            removerTudo(lista)
        elif opcao == 5:
            print('Saindo do programa.')
        else:
            print('Opção inválida. Tente novamente.')
            
main()
