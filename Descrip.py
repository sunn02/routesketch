import sys 

def generate_matrix(num_vertices,edges): 
    # "n" for the number or nodes
    # edges it is what connected the nodes
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
    min_distance = sys.maxsize #se inicia con el valor mas grande para encontrar la distancia minima en la busqueda
    min_index = -1 
    
    for vertex in range(len(distance)):
        if distance[vertex] < min_distance and not shortPathSet[vertex]: #si la distanica es menor que infinito y no esta en el arbol de caminos elegidos
            min_distance = distance[vertex] #la minima distacancia se vuelve a la encontrada
            min_index = vertex #guarda el indice del vertice
    return min_index

def dijkstra(num_vertices, graph, source):
    distance = [sys.maxsize] * num_vertices
    distance[source] = 0 #Confirma que la distancia entre el origen consigo mismo es 0 
    shortPathSet = [False] * num_vertices
    for _ in range(num_vertices):
        min_vertex = minDistance(distance, shortPathSet) #El vertice que contiene el minimo valor 
        shortPathSet[min_vertex] = True #ingresa el minimo valor en la lista de caminos
        for current_vertex in range(num_vertices): #recorre
            if graph[min_vertex][current_vertex] > 0 and not shortPathSet[current_vertex] and \
               distance[current_vertex] > distance[min_vertex] + graph[min_vertex][current_vertex]:
                
                distance[current_vertex] = distance[min_vertex] + graph[min_vertex][current_vertex] #
    return distance





# V1 = 3
# edges1 = [(0, 1), (1, 2), (2, 0)]
# adj_matrix1 = generate_matrix(V1, edges1)
# for row in adj_matrix1:
#     print(row)
# print()