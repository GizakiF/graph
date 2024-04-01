from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

mydata = genfromtxt('mycsv.csv', delimiter=',')
print(mydata)
print(type(mydata))
adjacency = mydata[1:,1:]
print(adjacency)

def show_graph_with_labels(adjacency_matrix, mylabels):
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    nx.draw(gr, node_size=500, labels=mylabels, with_labels=True)
    plt.show()

show_graph_with_labels(adjacency, make_label_dict(get_labels('mycsv.csv')))
