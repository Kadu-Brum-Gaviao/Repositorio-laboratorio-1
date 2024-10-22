fibonacci1 = 0
fibonacci2 = 1
resultado = 0

print(fibonacci1)
for i in range(10):
    resultado = fibonacci1 + fibonacci2
    print(resultado)
    fibonacci1 = fibonacci2
    fibonacci2 = resultado
