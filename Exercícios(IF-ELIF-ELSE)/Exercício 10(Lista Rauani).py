genero = input('Digite seu gênero: ').upper()
idade = float(input('Digite sua idade: '))


if (genero == 'MASCULINO') and (idade >= 18):
    print('Homem Adulto.')
elif (genero == 'FEMININO') and (idade >= 18):
    print('Mulher Adulta.')
elif idade < 18:
    print('Adolescente.')

