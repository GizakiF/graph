import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load data
input_data = pd.read_csv('mycsv.csv', index_col=0)

# Create a directed graph
G = nx.DiGraph(input_data.values)

# Draw the graph
pos = nx.spring_layout(G)  # you can also use other layout algorithms
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, arrowsize=20)
plt.show()

