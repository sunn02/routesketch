import sys

# Define the vertices with their coordinates
vertices = {
    (0, 0): 0,
    (1, 0): 1,
    (1, 1): 2,
    (0, 1): 3,
    (2, 1): 4,
    (1, 2): 5
}

# Define the edges (connecting the vertices)
edges = [
    ((0, 0), (1, 0)),
    ((0, 0), (0, 1)),
    ((1, 0), (1, 1)),
    ((1, 0), (2, 1)),
    ((1, 1), (1, 2)),
    ((0, 1), (1, 1))
]

def generate_matrix(num_vertices, edges, obstacles):
    matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    for (v1, v2) in edges:
        if v1 not in obstacles and v2 not in obstacles:
            i, j = vertices[v1], vertices[v2]
            matrix[i][j] = 1
            matrix[j][i] = 1
    return matrix

def min_distance(distance, short_path_set):
    min_distance = sys.maxsize
    min_index = -1
    for vertex in range(len(distance)):
        if distance[vertex] < min_distance and not short_path_set[vertex]:
            min_distance = distance[vertex]
            min_index = vertex
    return min_index

def dijkstra(num_vertices, graph, source):
    distance = [sys.maxsize] * num_vertices
    distance[source] = 0
    short_path_set = [False] * num_vertices
    for _ in range(num_vertices):
        min_vertex = min_distance(distance, short_path_set)
        short_path_set[min_vertex] = True
        for current_vertex in range(num_vertices):
            if graph[min_vertex][current_vertex] > 0 and not short_path_set[current_vertex] and \
               distance[current_vertex] > distance[min_vertex] + graph[min_vertex][current_vertex]:
                distance[current_vertex] = distance[min_vertex] + graph[min_vertex][current_vertex]
    return distance


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def print_graph_with_path(num_vertices, graph, source, destination, path, obstacles):
    print("Mapa con Ruta:")
    coord_map = {v: k for k, v in vertices.items()}
    max_x = max(coord[0] for coord in coord_map.values()) + 1
    max_y = max(coord[1] for coord in coord_map.values()) + 1
    grid = [['.' for _ in range(max_y)] for _ in range(max_x)]
    
    # Mark obstacles
    for obstacle in obstacles:
        if obstacle in coord_map:
            coord = coord_map[obstacle]
            grid[coord[0]][coord[1]] = '#'

    # Mark the path
    for node in path:
        if node in coord_map:
            coord = coord_map[node]
            grid[coord[0]][coord[1]] = '*'
    
    # Mark source and destination
    grid[source[0]][source[1]] = 'S'
    grid[destination[0]][destination[1]] = 'D'

    print(" ", " ".join(map(str, range(max_y))))
    for i in range(max_x):
        print(i, " ".join(grid[i]))

def find_vertex_by_coordinates(coords):
    return vertices.get(coords, -1)

# Example Usage
num_vertices = len(vertices)


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Solicitar al usuario que ingrese las coordenadas de obstáculos
obstacles = []
num_obstacles = int(input("Ingrese el número de obstáculos: "))
for _ in range(num_obstacles):
    obstacle_x, obstacle_y = map(int, input("Ingrese las coordenadas del obstáculo (x y): ").split())
    obstacle_coords = (obstacle_x, obstacle_y)
    if obstacle_coords in vertices:
        obstacles.append(obstacle_coords)
    else:
        print(f"Las coordenadas del obstáculo ({obstacle_x}, {obstacle_y}) no son válidas o no están en el gráfico.")

graph = generate_matrix(num_vertices, edges, obstacles)

# Solicitar al usuario que ingrese las coordenadas de inicio y fin
source_x, source_y = map(int, input("Ingrese las coordenadas de inicio (x y): ").split())
destination_x, destination_y = map(int, input("Ingrese las coordenadas de fin (x y): ").split())

source_coords = (source_x, source_y)
destination_coords = (destination_x, destination_y)

# Convertir coordenadas a índices de vértices
source_vertex = find_vertex_by_coordinates(source_coords)
destination_vertex = find_vertex_by_coordinates(destination_coords)

if source_vertex == -1 or destination_vertex == -1:
    print("Coordenadas de inicio o fin inválidas.")
else:
    distance = dijkstra(num_vertices, graph, source_vertex)

    path = []
    current_vertex = destination_vertex
    while current_vertex != source_vertex:
        path.append(current_vertex)
        min_distance = sys.maxsize
        next_vertex = None
        for i in range(num_vertices):
            if graph[current_vertex][i] and distance[i] < min_distance:
                min_distance = distance[i]
                next_vertex = i
        current_vertex = next_vertex
    path.append(source_vertex)
    path.reverse()

    # Imprimir el gráfico con la ruta
    print_graph_with_path(num_vertices, graph, source_coords, destination_coords, path, obstacles)

    # Imprimir la distancia de la ruta más corta al destino
    if distance[destination_vertex] < sys.maxsize:
        print(f"La distancia de la ruta más corta desde {source_coords} hasta {destination_coords} es {distance[destination_vertex]}")
    else:
        print(f"No hay ruta desde {source_coords} hasta {destination_coords}")
