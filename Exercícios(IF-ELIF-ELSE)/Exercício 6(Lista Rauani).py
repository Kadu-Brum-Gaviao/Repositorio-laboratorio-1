nome = input('Digite seu nome: ')
nota = float(input('Digite sua nota: '))

if nota < 5:
    print(f'A nota do aluno {nome} foi {nota}, ele foi reprovado!')
elif (nota >= 5) and (nota < 7):
    print(f'A nota do aluno {nome} foi {nota}, ele está de recuperação!')
elif (nota >= 7) and (nota <= 10):
    print(f'A nota do aluno {nome} foi {nota}, ele foi aprovado!')
elif (nota < 0) or (nota > 10):
    print('Erro no sistema!')
