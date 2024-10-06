fatorial = int(input('Digite um número: '))
multiplicador = 1
resultado = 1

while multiplicador <= fatorial:
    resultado = resultado * multiplicador
    multiplicador += 1
print(resultado)
