def generate_matrix(n,edges): 
    # "n" for the number or nodes
    # edges it is what connected the nodes
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    #For each edge (i,j)
    for edge in edges:
        i, j = edge
        matrix[i][j] = 1
        matrix[j][i] = 1
    return matrix

V1 = 3
edges1 = [(0, 1), (1, 2), (2, 0)]
adj_matrix1 = generate_matrix(V1, edges1)
for row in adj_matrix1:
    print(row)
print()