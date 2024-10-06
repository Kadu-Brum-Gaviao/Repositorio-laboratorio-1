a = 80000
b = 200000
anos = 0

while a < b:
    a *= 1.03
    b *= 1.015
    anos += 1

print(f'Tempo para a população do país A ultrapassar ou igualar a população do país B é: {anos}')
