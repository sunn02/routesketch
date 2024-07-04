def generate_empty_matrix(n):
    return [['.' for _ in range(n)] for _ in range(n)]

def imprimir_cuadricula(matrix):
    n = len(matrix)
    print("Mapa con Ruta:")
    encabezado = "  " + " ".join(str(i) for i in range(n))
    print(encabezado)
    
    for i in range(n):
        fila = str(i) + " "
        for j in range(n):
            fila += matrix[i][j] + " "
        print(fila)

def insertar_inicio_fin(matrix): 
    x_inicio = int(input("Ingrese la coordenada x del inicio: "))
    y_inicio = int(input("Ingrese la coordenada y del inicio: "))
    if 0 <= x_inicio < len(matrix) and 0 <= y_inicio < len(matrix[0]):
            matrix[x_inicio][y_inicio] = 'S'

    x_fin = int(input("Ingrese la coordenada x del fin: "))
    y_fin = int(input("Ingrese la coordenada y del fin: "))
    if 0 <= x_fin < len(matrix) and 0 <= y_fin < len(matrix[0]):
            matrix[x_fin][y_fin] = 'D'

def insertar_obstaculos(matrix):
    num_obstaculos = int(input("¿Cuántos obstáculos desea insertar? "))
    for _ in range(num_obstaculos):
        x = int(input("Ingrese la coordenada x del obstáculo: "))
        y = int(input("Ingrese la coordenada y del obstáculo: "))
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
            matrix[x][y] = 'X'



n = int(input("Inserte el numero de matriz:"))
# Generar la matriz vacía
matrix = generate_empty_matrix(n)
imprimir_cuadricula(matrix)
insertar_inicio_fin(matrix)
insertar_obstaculos(matrix)
imprimir_cuadricula(matrix)

