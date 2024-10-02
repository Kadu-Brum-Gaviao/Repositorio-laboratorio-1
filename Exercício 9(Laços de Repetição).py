elevador_A_usos = 0
elevador_B_usos = 0
elevador_C_usos = 0

for i in range(10):
    opcaoElevador = input('Escolha um elevador(A/B/C): ').upper()
    if opcaoElevador == 'A':
        elevador_A_usos += 1
    elif opcaoElevador == 'B':
        elevador_B_usos += 1
    elif opcaoElevador == 'C':
        elevador_C_usos += 1
    else:
        print('Não usa o elevador.')

total_usos = elevador_A_usos + elevador_B_usos + elevador_C_usos

if total_usos > 0:
    porcentagemElevadorA = (elevador_A_usos / total_usos) * 100
    porcentagemElevadorB = (elevador_B_usos / total_usos) * 100
    porcentagemElevadorC = (elevador_C_usos / total_usos) * 100
else:
    porcentagemElevadorA = porcentagemElevadorB = porcentagemElevadorC = 0


print(f'Quantidade de morador que usam o Elevador A: {elevador_A_usos}')
print(f'Quantidade de morador que usam o Elevador B: {elevador_B_usos}')
print(f'Quantidade de morador que usam o Elevador C: {elevador_C_usos}')
print(f'Porcentagem de uso, Elevador A: {porcentagemElevadorA}')
print(f'Porcentagem de uso, Elevador B: {porcentagemElevadorB}')
print(f'Porcentagem de uso, Elevador C: {porcentagemElevadorC}')