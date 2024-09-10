"""
Faça um algoritmo que leia as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:
    Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0                      A
      Entre 7.5 e 9.0                        B
      Entre 6.0 e 7.5                        C
      Entre 4.0 e 6.0                        D
      Entre 4.0 e zero                      E
O algoritmo deve mostrar as notas, a média, o conceito correspondente e a mensagem
“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

nomeAluno = input('Qual é o nome do aluno: ')

nota1 = float(input(f'Qual a primeira nota do {nomeAluno}: '))
nota2 = float(input(f'Qual a segunda nota do {nomeAluno}: '))
nota3 = float(input(f'Qual a terceira nota do {nomeAluno}: '))

media = (nota1 + nota2 + nota3) / 3

if media < 0 and media > 10:
    print('Erro no sistema!')
else:
    print(f'A média do aluno {nomeAluno} é {media:.2f}!')

if media >= 9 and media <= 10:
    print(f'Parabens! A nota do aluno {nomeAluno} foi A e ele foi aprovado!')
elif media >= 7.5 and media < 9:
    print(f'Parabens! A nota do aluno {nomeAluno} foi B e ele foi aprovado!')
elif media >= 6 and media < 7.5:
    print(f'Parabens! A nota do aluno {nomeAluno} foi C e ele foi aprovado!')
elif media >= 4 and media < 6:
    print(f'Infelizmente a nota do aluno {nomeAluno} foi D e ele foi reprovado...')
elif media >= 0 and media < 4:
    print(f'Infelizmente a nota do aluno {nomeAluno} foi E e ele foi reprovado...')
