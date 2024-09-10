"""
Faça um algoritmo que leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. Também solicite qual a % de frequência e aula, verifique e apresente a seguinte mensagem:
Aprovado: Nota maior ou igual a 7,0 e frequência igual ou superior a 75%.
Exame: Nota maior ou igual a 4,0 e menor que 7,0 e frequência superior a 75%.
Reprovado: Nota inferior a 4,0 ou frequência menor que 75%.

"""

nomeAluno = input('Qual é o nome do aluno: ')
notaParcial1 = float(input(f'Qual a primeira nota do {nomeAluno}: '))
notaParcial2 = float(input(f'Qual a segunda nota do {nomeAluno}: '))
mediaAluno = (notaParcial1 + notaParcial2) / 2

frequenciaAluno = int(input(f'Frequência do aluno (%): '))

if (mediaAluno < 0 or mediaAluno > 10) and (frequenciaAluno < 0 or frequenciaAluno > 100):
    print('Erro no sistema!')
else:
    print(f'A média do aluno é {mediaAluno}!')
    print(f'A frequencia do {nomeAluno} é {frequenciaAluno}%!')

if (mediaAluno >= 7) and (frequenciaAluno >= 75):
    print(f'Aluno {nomeAluno} foi aprovado!')
elif (mediaAluno >= 4) and (frequenciaAluno > 75):
    print(f'Aluno {nomeAluno} ficou de exame...')
elif (mediaAluno < 4) or (frequenciaAluno < 75):
    print(f'Aluno {nomeAluno} foi reprovado...')
