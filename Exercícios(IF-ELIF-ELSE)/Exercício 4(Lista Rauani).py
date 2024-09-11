ano = int(input('Digite um ano: '))

if (ano % 4 == 0) and not (ano % 100 == 0):
    print(f'O ano {ano} divisivel por 4 e não é divisivel por 100, então ele é bissexto!')
elif ano % 400 == 0:
    print(f'O ano {ano} divisivel por 400, então ele é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
