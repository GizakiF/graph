import math


def floyd_warshall(graph):
  """
  Implements the Floyd-Warshall algorithm to find the shortest paths
  between all pairs of nodes in a weighted graph.

  Args:
      graph: A list of lists representing the adjacency matrix of the graph.
              Each inner list represents the edges connected to a node.
              Values in the inner list represent the weight of the edge,
              or infinity (math.inf) if there's no edge.

  Returns:
      A list of lists representing the distance matrix with the shortest
      distances between all pairs of nodes.
  """
  # Number of nodes in the graph
  n = len(graph)

  # Initialize the distance matrix with the original weights
  distance_matrix = graph.copy()

  # Use math.inf to represent no edge
  for i in range(n):
    for j in range(n):
      if distance_matrix[i][j] == 0 and i != j:
        distance_matrix[i][j] = math.inf

  print("Before the Operation")
  for row in distance_matrix:
      print(row)
  # Consider each node as an intermediate point
  for k in range(n):
    for i in range(n):
      for j in range(n):
        # Check if going through node k gives a shorter path
#        distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])
#to do: add a string to append each vertices' shortest path from point A to B
        if distance_matrix[i][j] > distance_matrix[i][k] + distance_matrix[k][j]:
             distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]
  return distance_matrix

# Example usage
graph = [
  [0, 3, math.inf, 7],
  [8, 0, 2, math.inf],
  [5, 0, 0, 1],
  [2, math.inf, math.inf, 0]
]

# Find shortest distances between all pairs
distance_matrix = floyd_warshall(graph)
print("After the Operation")
# Print the distance matrix
for row in distance_matrix:
  print(row)  


