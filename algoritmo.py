import sys

#use n for the number of vertices and vertex for iterating over vertices

def generate_matrix(num_vertices,edges): 
    # "n" for the number of vertices
    # edges it is what connected the vertices
    matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    #For each edge (i,j)
    for edge in edges:
        i, j = edge
        matrix[i][j] = 1
        matrix[j][i] = 1
    return matrix

def minDistance(distance, shortPathSet):
    #  Find the vertex with the minimum distance value from the set of vertices
    # not yet included in the shortest path tree.
    min_distance = sys.maxsize # infinite
    min_index = -1 

    for vertex in range(len(distance)):
        if distance[vertex] < min_distance and not shortPathSet[vertex]:
            min_distance = distance[vertex]
            min_index = vertex 
    return min_index


def dijkstra(num_vertices,graph,source):
    distance = [sys.maxsize] * num_vertices
    distance[source] = 0 
    shortPathSet = [False] * num_vertices

    for _ in range(num_vertices):
        min_vertex = minDistance(distance, shortPathSet)

        shortPathSet[min_vertex] = True
        for current_vertex in range(num_vertices):
            if graph[min_vertex][current_vertex] > 0 and shortPathSet[current_vertex] == False and \
                distance[current_vertex] > distance[min_vertex] + graph[min_vertex][current_vertex]:
                distance[current_vertex] = distance[min_vertex] + graph[min_vertex][current_vertex]
            
    return distance

def print_solution(distance):
    """
    Print the distances from the source to all vertices.
    """
    print("Vertex \tDistance from Source")
    for vertex, dist in enumerate(distance):
        print(f"{vertex} \t{dist if dist < sys.maxsize else 'Inf'}")

num_vertices = 4
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
graph = generate_matrix(num_vertices, edges)
source_vertex = 0

distance = dijkstra(num_vertices,graph,source_vertex)
print_solution(distance)

# V1 = 3
# edges1 = [(0, 1), (1, 2), (2, 0)]
# adj_matrix1 = generate_matrix(V1, edges1)
# for row in adj_matrix1:
#     print(row)
# print()





