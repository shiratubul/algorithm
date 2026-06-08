import networkx as nx
import pandas as pd

G = nx.petersen_graph()

print("Adjacency List:\n")

for node in G.nodes():
    neighbors = list(G.neighbors(node))
    print(f"{node}: {neighbors}")


print("\nDegree:\n")

for node in G.nodes():
    print(f"Vertex {node}: degree = {G.degree(node)}")



adj_matrix = nx.to_pandas_adjacency(G, dtype=int)

adj_matrix.to_html("adjacency_matrix.html")

