#Soma de matrizes

matriz1 = [[0] * 2 for i in range(2)]
matriz2 = [[0] * 2 for i in range(2)]
matriz_soma = [[0] * 2 for i in range(2)]

print ("Matriz 1")
for i in range(2):
    for j in range(2):
        matriz1[i][j] = int(input(f"Digite os valores da matriz 1 [{i}][{j}]: "))

print ("Matriz 2")
for i in range(2):
    for j in range(2):
        matriz2[i][j] = int(input(f"Digite os valores da matriz 2 [{i}][{j}]: "))
        matriz_soma[i][j] = matriz1[i][j] + matriz2[i][j]

print("A soma das matrizes é:")
for i in range(2):
    for j in range(2):
        print(matriz_soma[i][j], end = " ")
    print()

