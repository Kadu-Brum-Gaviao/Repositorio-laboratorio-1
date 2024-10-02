entre_30_e_90 = 0

for i in range(10):
    num = int(input('Digite um número: '))
    if (num > 30) and (num < 90):
        entre_30_e_90 += 1
print(f'Quantidade de números entre 30 a 90: {entre_30_e_90}')
