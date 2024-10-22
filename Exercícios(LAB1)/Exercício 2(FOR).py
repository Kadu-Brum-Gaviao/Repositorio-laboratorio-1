media = 0
soma = 0
quantidade = 0
for i in range(10):
    try:
        numero = int(input('Digite um número: '))
        soma = soma + numero
        quantidade += 1
    except:
        print('Tente novamente...')

media = soma / quantidade
print(media)