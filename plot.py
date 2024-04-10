import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

matrix = np.array([
    [0, 4, 0, 2],
    [4, 0, 3, 0],
    [0, 3, 0, 1],
    [2, 0, 1, 0]
])

G = nx.from_numpy_array(matrix)

# Create a dictionary to map node indices to labels
label_mapping = {i: chr(65 + i) for i in range(len(G.nodes()))}

# Draw the graph with node labels and no background color for nodes
pos = nx.circular_layout(G)  # Fixed layout
nx.draw(G, pos=pos, with_labels=True, labels=label_mapping, font_size='16', node_color='white')

# Create a dictionary to map edge indices to weights
edge_labels = nx.get_edge_attributes(G, 'weight')

# Calculate midpoint coordinates for each edge
for edge, weight in edge_labels.items():
    u, v = edge
    x = (pos[u][0] + pos[v][0]) / 2
    y = (pos[u][1] + pos[v][1]) / 2
    plt.text(x, y, str(weight), fontsize=12, color='red', fontweight='bold',
             horizontalalignment='center', verticalalignment='center')

plt.axis('off')
plt.show()