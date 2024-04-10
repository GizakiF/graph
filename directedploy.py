import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

matrix = np.array([
  [0, 0, -2, 0],
  [4, 0, 3, 0],
  [0, 0, 0, 2],
  [0, -1, 0, 0]
])

G = nx.from_numpy_array(matrix, create_using=nx.DiGraph())

# Create a dictionary to map node indices to labels
label_mapping = {i: chr(48 + i) for i in range(len(G.nodes()))}

# Draw the graph with node labels and no background color for nodes
pos = nx.circular_layout(G)  # Fixed layout
nx.draw(G, pos=pos, with_labels=True, labels=label_mapping, node_color='none')

# Create a dictionary to map edge indices to weights
edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges()}

# Draw edges with background color
# nx.draw_networkx_edges(G, pos=pos, width=6, edge_color='gray')

# Draw edges with thinner line to overlay
nx.draw_networkx_edges(G, pos=pos, width=2, edge_color='black')

# Calculate midpoint coordinates for each edge
for edge, weight in edge_labels.items():
    u, v = edge
    x = (pos[u][0] + pos[v][0]) / 2
    y = (pos[u][1] + pos[v][1]) / 2
    
    # Add a small offset to the coordinates
    offset_x, offset_y = 0.05 * (pos[v][1] - pos[u][1]), -0.05 * (pos[v][0] - pos[u][0])
    
    # Draw white rectangle behind text
    plt.text(x + offset_x, y + offset_y, str(weight), fontsize=12, color='white', fontweight='bold',
             horizontalalignment='center', verticalalignment='center',
             bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.2'))
    plt.text(x + offset_x, y + offset_y, str(weight), fontsize=12, color='red', fontweight='bold',
             horizontalalignment='center', verticalalignment='center')

plt.axis('off')
plt.show()