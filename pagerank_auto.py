import networkx as nx
import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv('./data/web-Stanford.txt', sep="\t", header=None, skiprows=4)
    G = nx.DiGraph()
    for i in range(len(data)):
        G.add_node(data.iloc[i][0])
        G.add_node(data.iloc[i][1])
        G.add_edge(data.iloc[i][0], data.iloc[i][1])

    pr = nx.pagerank(G, alpha=0.9)
    print(pr)