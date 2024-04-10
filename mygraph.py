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
      A tuple containing three lists:
          - distance_matrix: A list of lists representing the distance matrix
                             with the shortest distances between all pairs of nodes.
          - predecessor_matrix: A list of lists where predecessor_matrix[i][j]
                                stores the predecessor node in the shortest path
                                from vertex i to vertex j.
          - shortest_paths: A dictionary where shortest_paths[i][j] stores the
                             shortest path (list of vertices) from vertex i to vertex j.
  """
  # Number of nodes in the graph
  n = len(graph)

  # Initialize the distance matrix with the original weights
  distance_matrix = graph.copy()

  # Initialize the predecessor matrix with -1 (no predecessor initially)
  predecessor_matrix = [[-1] * n for _ in range(n)]

  # Initialize the shortest paths dictionary
  shortest_paths = {i: {} for i in range(n)}  # Empty dictionary for each source

  # Use math.inf to represent no edge
  for i in range(n):
    for j in range(n):
      if distance_matrix[i][j] == 0 and i != j:
        distance_matrix[i][j] = math.inf

  # Consider each node as an intermediate point
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if distance_matrix[i][i] < 0:
            print("Negative-weight cycle found")
            return None
        # Check if going through node k gives a shorter path
        if distance_matrix[i][j] > distance_matrix[i][k] + distance_matrix[k][j]:
          distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]
          predecessor_matrix[i][j] = k  # Update predecessor

  # Reconstruct shortest paths from predecessor information
  for i in range(n):
    for j in range(n):
      if i != j and distance_matrix[i][j] != math.inf:
        # Reconstruct path from i to j using predecessor_matrix
        path = [j]
        current = predecessor_matrix[i][j]
        while current != -1:
          path.append(current)
          current = predecessor_matrix[i][current]
        path.reverse()  # Reverse to get the path from source to destination
        shortest_paths[i][j] = path

  return distance_matrix, predecessor_matrix, shortest_paths

# Example usage
#graph = [
#  [0, 2, 4, math.inf],
#  [2, 0, 3, 4],
#  [4, 3, 0, 1],
#  [math.inf, 4, 1, 0]
#]

# graph = [
#   [0, math.inf, -2, 0],
#   [4, 0, 3, 0],
#   [0, 0, 0, 2],
#   [0, -1, 0, 0]
#]
#graph = [
#  [0, 2, 4, math.inf],
#  [2, 0, 3, 4],
#  [4, 3, 0, 1],
#  [math.inf, -5, 1, 0]  # Introduce a negative weight cycle here
#]
graph = [
   [0, 4, math.inf, 2],
   [4, 0, 3, math.inf],
   [math.inf, 3, 0, 1],
   [2, math.inf, 1, 0]
] 
# Find shortest distances, predecessors, and paths
distance_matrix, predecessor_matrix, shortest_paths = floyd_warshall(graph)

# Print the distance matrix
print("Distance Matrix:")
for row in distance_matrix:
  print(row)

# Accessing shortest paths
for source in range(len(graph)):
  print(f"\nShortest paths from vertex {source}:")
  for destination in range(len(graph)):
    if source != destination and distance_matrix[source][destination] != math.inf:
      path = shortest_paths[source][destination]
      path.insert(0, source)
      print(f"{source} -> {destination}: {path}")
    else:
      print(f"{source} -> {destination}: No path exists")
