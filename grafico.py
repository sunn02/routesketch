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

def insertar_obstaculos(matrix, obstaculos):
    for obstaculo in obstaculos:
        i, j = obstaculo
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
            matrix[i][j] = 'X'

n = int(input("Inserte el numero de matriz:"))
# Generar la matriz vacía
matrix = generate_empty_matrix(n)

num_obstaculos = int(input("¿Cuántos obstáculos desea insertar? "))
# Pedir al usuario las coordenadas de los obstáculos
obstaculos = []
for _ in range(num_obstaculos):
    x = int(input("Ingrese la coordenada x del obstáculo: "))
    y = int(input("Ingrese la coordenada y del obstáculo: "))
    obstaculos.append((x, y))

# Insertar los obstáculos en la matriz
insertar_obstaculos(matrix, obstaculos)
# Imprimir la cuadrícula con los obstáculos
imprimir_cuadricula(matrix)

