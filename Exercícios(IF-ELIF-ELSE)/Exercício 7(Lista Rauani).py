senha = input('Digite sua senha: ')

if (len(senha) > 8) and ('@' in senha):
    print(f'Senha válida!')
else:
    print('Senha está inválida!')