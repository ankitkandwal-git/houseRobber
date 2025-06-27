def construct_adjacency_matrix(n, edges):
   adj_matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

   for f, t in edges:
       adj_matrix[f][t] = 1
       adj_matrix[t][f] = 1

   return adj_matrix

if __name__ == "__main__":
   n, e = map(int, input().split())

   edges = []
   for _ in range(e):
       f, t = map(int, input().split())
       edges.append((f, t))

   adj_matrix = construct_adjacency_matrix(n, edges)

   for i in range(1, n + 1):
       for j in range(1, n + 1):
           print(adj_matrix[i][j], end=" ")
       print()