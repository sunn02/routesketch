import sys 
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
    return (x_inicio, y_inicio), (x_fin, y_fin)

def insertar_obstaculos(matrix):
    num_obstaculos = int(input("¿Cuántos obstáculos desea insertar? "))
    for _ in range(num_obstaculos):
        x = int(input("Ingrese la coordenada x del obstáculo: "))
        y = int(input("Ingrese la coordenada y del obstáculo: "))
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
            matrix[x][y] = 'X'

def generate_matrix(num_vertices,edges): 
    matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    for edge in edges:
        i, j = edge
        matrix[i][j] = 1
        matrix[j][i] = 1
    return matrix

def minDistance(distance, shortPathSet):
    min_distance = sys.maxsize 
    min_index = -1 

    for vertex in range(len(distance)):
        if distance[vertex] < min_distance and not shortPathSet[vertex]:
            min_distance = distance[vertex]
            min_index = vertex 
    return min_index

def dijkstra(num_vertices, graph, source):
    distance = [sys.maxsize] * num_vertices
    distance[source] = 0 
    shortPathSet = [False] * num_vertices
    predecessor = [-1] * num_vertices
    for _ in range(num_vertices):
        min_vertex = minDistance(distance, shortPathSet)
        shortPathSet[min_vertex] = True
        for current_vertex in range(num_vertices):
            if graph[min_vertex][current_vertex] > 0 and not shortPathSet[current_vertex] and \
                distance[current_vertex] > distance[min_vertex] + graph[min_vertex][current_vertex]:
                distance[current_vertex] = distance[min_vertex] + graph[min_vertex][current_vertex]
                predecessor[current_vertex] = min_vertex 

    return distance, predecessor

def obtener_vertices_edges(matrix):
    vertices = []
    edges = []
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 'X':
                vertices.append((i, j))
                if i > 0 and matrix[i-1][j] != 'X':
                    edges.append(((i, j), (i-1, j)))
                if i < n-1 and matrix[i+1][j] != 'X':
                    edges.append(((i, j), (i+1, j)))
                if j > 0 and matrix[i][j-1] != 'X':
                    edges.append(((i, j), (i, j-1)))
                if j < n-1 and matrix[i][j+1] != 'X':
                    edges.append(((i, j), (i, j+1)))
    return vertices, edges

def convertir_a_indice(vertices, coord):
    return vertices.index(coord)

def get_shortest_path(predecessor, start, end):
    path = []
    while end != -1:
        path.append(end)
        end = predecessor[end]
    path.reverse()
    return path

def marcar_camino(matrix, path):
    for (x, y) in path:
        if matrix[x][y] not in ('S', 'D', 'X'):
            matrix[x][y] = '*'

n = int(input("Inserte el número de matriz: "))

matrix = generate_empty_matrix(n)
imprimir_cuadricula(matrix)

insertar_obstaculos(matrix)
inicio, fin = insertar_inicio_fin(matrix)
imprimir_cuadricula(matrix)

vertices, edges = obtener_vertices_edges(matrix)
num_vertices = len(vertices)

edges = [(convertir_a_indice(vertices, edge[0]), convertir_a_indice(vertices, edge[1])) for edge in edges]
graph = generate_matrix(num_vertices, edges)

inicio_idx = convertir_a_indice(vertices, inicio)
fin_idx = convertir_a_indice(vertices, fin)

distances, predecessor = dijkstra(num_vertices, graph, inicio_idx)

# Obtener el camino más corto
path_indices = get_shortest_path(predecessor, inicio_idx, fin_idx)
path = [vertices[i] for i in path_indices]

# Marcar el camino más corto en la matriz
marcar_camino(matrix, path)

# Imprimir la cuadrícula con el camino más corto
imprimir_cuadricula(matrix)
