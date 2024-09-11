diaDoAno = int(input('Digite um dia entre 0 e 366: '))

if (diaDoAno > 0) and (diaDoAno <= 31):
    print('O més desses dias é janeiro.')
elif diaDoAno <= 60:
    print('O mês desses dias é fevereiro.')
elif diaDoAno <= 91:
    print('O mês desses dias é março.')
elif diaDoAno <= 121:
    print('O mês desses dias é abril.')
elif diaDoAno <= 152:
    print('O mês desses dias é maio.')
elif diaDoAno <= 182:
    print('O mês desses dias é junho.')
elif diaDoAno <= 213:
    print('O mês desses dias é julho.')
elif diaDoAno <= 244:
    print('O mês desses dias é agosto.')
elif diaDoAno <= 274:
    print('O mês desses dias é setembro.')
elif diaDoAno <= 305:
    print('O mês desses dias é outubro.')
elif diaDoAno <= 335:
    print('O mês desses dias é novembro.')
elif diaDoAno <= 366:
    print('O mês desses dias é dezembro.')
else:
    print('Erro! Dia invalido.4')
