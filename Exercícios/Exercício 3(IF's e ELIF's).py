"""
Um professor quer fazer um algoritmo para testar se uma questão de
múltipla escolha está certa. Para isso, leia a questão assinalada
pelo aluno e verifique:

A - resposta errada
B - resposta certa
C - resposta errada
D - resposta errada

"""

"""
Um homem em uma competição de comida come 97 hamburgueres.
Na segunda vez que ele compete, ele come 128. Quantos hamburgueres foram 
consumidos a mais que a primeira vez.
"""

a = 32
b = 31
c = 33
d = 30

alternativas = input('Digite uma das alterativas: ').lower()

if alternativas not in ('a', 'b', 'c', 'd'):
    print('Alternativa Invalida...')

if alternativas == 'b':
    print('Resposta correta!')
else:
    print('Resposta Errada!')
