cont_10_a_20 = 0
cont_fora = 0

for i in range(10):
    num = float(input('Digite um número: '))
    while num < 0:
        print('Erro. O número não pode ser negativo. Tente novamente.')
        num = float(input('Digite um número: '))
    if num >= 10 and num <= 20:
        cont_10_a_20 += 1
    else:
        cont_fora += 1


print('Números no intervalo[10, 20]: ', cont_10_a_20)
print('Números fora do intervalo: ', cont_fora)
