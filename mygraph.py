import pandas as pd
import networkx as nx
input_data = pd.read_csv('mycsv.csv', index_col=0)
G = nx.DiGraph(input_data.values)
nx.draw(G)
