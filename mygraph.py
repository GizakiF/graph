import math

def floyd_warshall(graph):
  """
  Implements the Floyd-Warshall algorithm to find the shortest paths
  and predecessor information between all pairs of nodes in a weighted graph.

  Args:
      graph: A list of lists representing the adjacency matrix of the graph.
              Each inner list represents the edges connected to a node.
              Values in the inner list represent the weight of the edge,
              or infinity (math.inf) if there's no edge.

  Returns:
      A tuple containing two lists:
          - distance_matrix: A list of lists representing the distance matrix
                             with the shortest distances between all pairs of nodes.
          - predecessor_matrix: A list of lists where predecessor_matrix[i][j]
                                stores the predecessor node in the shortest path
                                from vertex i to vertex j.
  """
  # Number of nodes in the graph
  n = len(graph)

  # Initialize the distance matrix with the original weights
  distance_matrix = graph.copy()

  # Initialize the predecessor matrix with -1 (no predecessor initially)
  predecessor_matrix = [[-1] * n for _ in range(n)]

  # Use math.inf to represent no edge
  for i in range(n):
    for j in range(n):
      if distance_matrix[i][j] == 0 and i != j:
        distance_matrix[i][j] = math.inf

  # Consider each node as an intermediate point
  for k in range(n):
    for i in range(n):
      for j in range(n):
        # Check if going through node k gives a shorter path
        if distance_matrix[i][j] > distance_matrix[i][k] + distance_matrix[k][j]:
          distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]
          predecessor_matrix[i][j] = k  # Update predecessor

  return distance_matrix, predecessor_matrix

# Example usage
graph = [
  [0, 2, 4, math.inf],
  [2, 0, 3, 4],
  [4, 3, 0, 1],
  [math.inf, 4, 1, 0]
]

# Find shortest distances and predecessors
distance_matrix, predecessor_matrix = floyd_warshall(graph)

# Print the distance matrix
print("Distance Matrix:")
for row in distance_matrix:
  print(row)

# Print the predecessor matrix (example usage for shortest path retrieval)
print("\nPredecessor Matrix:")
for row in predecessor_matrix:
  print(row)

# Example: Find shortest path from vertex 0 to vertex 3
source = 0
destination = 3

path = []
while destination != -1:
  path.append(destination)
  destination = predecessor_matrix[source][destination]

path.reverse()  # Reverse to get the path from source to destination
print(f"\nShortest path from {source} to {destination}: {path}")

