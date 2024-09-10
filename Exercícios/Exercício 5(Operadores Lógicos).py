"""
Faça um script que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O script deve no final emitir uma classificação sobre a participação da
pessoa no crime. Se a pessoa responder positivamente a 2 questões
ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
nomePessoa = input('Digite o nome da pessoa: ')

perguntas = [
    "Telefonou para a vítima? (s/n): ",
    "Esteve no local do crime? (s/n): ",
    "Mora perto da vítima? (s/n): ",
    "Devia para a vítima? (s/n): ",
    "Já trabalhou com a vítima? (s/n): "
]

respostasSim = 0

for pergunta in perguntas:
    resposta = input(pergunta).strip().lower()
    while resposta not in ('s', 'n'):
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")
        resposta = input(pergunta).strip().lower()
    if resposta == 's':
        respostasSim += 1

if respostasSim == 2:
    print(f'{nomePessoa} é classificada como suspeita...')
elif respostasSim == 3 or respostasSim == 4:
    print(f'{nomePessoa} é classificada como cúmplice...')
elif respostasSim == 5:
    print(f'{nomePessoa} é o assassino!')
else:
    print(f'{nomePessoa} é inocente!')
