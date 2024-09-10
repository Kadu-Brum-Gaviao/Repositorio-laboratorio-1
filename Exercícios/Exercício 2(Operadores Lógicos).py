"""
Faça um script que peça os 3 lados de um triângulo.
O script deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é:
equilátero, isósceles ou escaleno.

Dicas:
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

triangulolado1 = float(input('Digite o valor do primeiro lado do triângulo: '))
triangulolado2 = float(input('Digite o valor do segundo lado do triângulo: '))
triangulolado3 = float(input('Digite o valor do terceiro lado do triângulo: '))

if (triangulolado1 + triangulolado2 > triangulolado3) and \
   (triangulolado1 + triangulolado3 > triangulolado2) and \
   (triangulolado2 + triangulolado3 > triangulolado1):
    print('Os valores formam um triângulo!')

    if triangulolado1 == triangulolado2 == triangulolado3:
        print('É um triângulo equilátero!')
    elif (triangulolado1 == triangulolado2) or (triangulolado1 == triangulolado3) or (triangulolado2 == triangulolado3):
        print('É um triângulo isósceles!')
    elif triangulolado1 != triangulolado2 != triangulolado3:
        print('É um triângulo escaleno!')
    else:
        print('Não é um triângulo!')
else:
    print('Os valores não formam um triângulo!')
