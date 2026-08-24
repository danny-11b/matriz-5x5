matriz = [[0 for _ in range(5)] for _ in range(5)]

# Ingresar valores con bucles anidados
for i in range(5):
    for j in range(5):
        valor = int(input(f"Ingrese el valor para la posición [{i+1}][{j+1}]: "))
        matriz[i][j] = valor

# Mostrar la matriz organizada
print("\nMatriz ingresada:")
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end="\t")
    print()