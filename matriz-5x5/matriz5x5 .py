matriz = [[0 for _ in range(4)] for _ in range(4)]

for i in range(5):
    for j in range(5):
        valor = int(input(f"Ingrese los 25 valores para la matriz [{i}][{j}]: "))
        matriz[i][j] = valor

print("\nMatriz ingresada:")
for i in range(4):
    for j in range(4):
        print(matriz[i][j], end="\t")
    print()
