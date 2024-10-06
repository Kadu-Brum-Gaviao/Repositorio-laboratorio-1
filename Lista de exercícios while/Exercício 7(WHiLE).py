base = int(input('Digite um número: '))
expoente = int(input('Digite um número: '))
contador = 0
resultado = base

while contador < expoente - 1:
    resultado = resultado * base
    contador += 1
print(resultado)
